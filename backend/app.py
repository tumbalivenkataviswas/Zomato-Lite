from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import logging

app = Flask(__name__)
CORS(app)  # Allow only the frontend origin

logging.basicConfig(level=logging.DEBUG)

def get_db_connection():
    conn = sqlite3.connect('zomato.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET'])
def home():
    return "Zomato API is running!"

@app.route('/restaurants/<int:restaurant_id>/reviews', methods=['GET'])
def get_reviews(restaurant_id):
    conn = get_db_connection()
    reviews = conn.execute('SELECT * FROM reviews WHERE restaurant_id = ?', (restaurant_id,)).fetchall()
    conn.close()
    return jsonify([dict(review) for review in reviews])

@app.route('/reviews', methods=['GET'])
def get_all_reviews():
    conn = get_db_connection()
    reviews = conn.execute('SELECT * FROM reviews').fetchall()
    conn.close()
    return jsonify([dict(review) for review in reviews])

@app.route('/restaurants/<int:id>/reviews', methods=['POST'])
def add_review(id):
    new_review = request.get_json()
    name = new_review['name']
    rating = new_review['rating']
    review = new_review['review']
    conn = get_db_connection()
    conn.execute('INSERT INTO reviews (restaurant_id, name, rating, review) VALUES (?, ?, ?, ?)',
                 (id, name, rating, review))
    conn.commit()
    conn.close()
    return '', 201

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    try:
        conn = get_db_connection()
        restaurant = conn.execute('SELECT * FROM restaurants WHERE id = ?', (id,)).fetchone()
        conn.close()
        if restaurant is None:
            app.logger.debug(f'Restaurant with ID {id} not found')
            return jsonify({'error': 'Restaurant not found'}), 404
        return jsonify(dict(restaurant))
    except Exception as e:
        app.logger.error(f'Error occurred: {e}')
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    try:
        conn = get_db_connection()
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        offset = (page - 1) * per_page
        search_term = request.args.get('search', '', type=str).lower()
        min_rating = request.args.get('min_rating', 0, type=float)
        max_rating = request.args.get('max_rating', 5, type=float)
        cuisine = request.args.get('cuisine', '', type=str).lower()
        min_cost = request.args.get('min_cost', 0, type=float)
        max_cost = request.args.get('max_cost', 10000, type=float)  # Set a reasonable upper limit

        # Ensure the search term is handled properly
        search_term = f'%{search_term}%'
        cuisine = f'%{cuisine}%'

        query = '''
            SELECT DISTINCT * FROM restaurants 
            WHERE LOWER(name) LIKE ? 
              AND aggregate_rating BETWEEN ? AND ?
              AND LOWER(cuisines) LIKE ?
              AND average_cost_for_two BETWEEN ? AND ?
            LIMIT ? OFFSET ?
        '''
        params = (search_term, min_rating, max_rating, cuisine, min_cost, max_cost, per_page, offset)
        
        restaurants = conn.execute(query, params).fetchall()
        conn.close()
        return jsonify([dict(row) for row in restaurants])
    except Exception as e:
        app.logger.error(f'Error occurred: {e}')
        return jsonify({'error': 'An error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5008)
