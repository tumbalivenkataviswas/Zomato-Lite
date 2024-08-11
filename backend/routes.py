from flask import Blueprint, jsonify, request
from models import Restaurant, Review, db

api = Blueprint('api', __name__)

@api.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'country_code': restaurant.country_code,
        'city': restaurant.city,
        'address': restaurant.address,
        'locality': restaurant.locality,
        'locality_verbose': restaurant.locality_verbose,
        'longitude': restaurant.longitude,
        'latitude': restaurant.latitude,
        'cuisines': restaurant.cuisines,
        'average_cost_for_two': restaurant.average_cost_for_two,
        'currency': restaurant.currency,
        'has_table_booking': restaurant.has_table_booking,
        'has_online_delivery': restaurant.has_online_delivery,
        'is_delivering_now': restaurant.is_delivering_now,
        'switch_to_order_menu': restaurant.switch_to_order_menu,
        'price_range': restaurant.price_range,
        'aggregate_rating': restaurant.aggregate_rating,
        'rating_color': restaurant.rating_color,
        'rating_text': restaurant.rating_text,
        'votes': restaurant.votes
    })

@api.route('/restaurants', methods=['GET'])
def get_restaurants():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    search_term = request.args.get('search', '', type=str)

    query = Restaurant.query

    if search_term:
        query = query.filter(Restaurant.name.ilike(f'%{search_term}%'))

    restaurants = query.paginate(page, per_page, error_out=False)

    return jsonify({
        'restaurants': [{
            'id': restaurant.id,
            'name': restaurant.name,
            'country_code': restaurant.country_code,
            'city': restaurant.city,
            'address': restaurant.address,
            'locality': restaurant.locality,
            'locality_verbose': restaurant.locality_verbose,
            'longitude': restaurant.longitude,
            'latitude': restaurant.latitude,
            'cuisines': restaurant.cuisines,
            'average_cost_for_two': restaurant.average_cost_for_two,
            'currency': restaurant.currency,
            'has_table_booking': restaurant.has_table_booking,
            'has_online_delivery': restaurant.has_online_delivery,
            'is_delivering_now': restaurant.is_delivering_now,
            'switch_to_order_menu': restaurant.switch_to_order_menu,
            'price_range': restaurant.price_range,
            'aggregate_rating': restaurant.aggregate_rating,
            'rating_color': restaurant.rating_color,
            'rating_text': restaurant.rating_text,
            'votes': restaurant.votes
        } for restaurant in restaurants.items],
        'total': restaurants.total,
        'pages': restaurants.pages,
        'current_page': restaurants.page
    })

@api.route('/restaurants/<int:id>/reviews', methods=['GET'])
def get_reviews(id):
    reviews = Review.query.filter_by(restaurant_id=id).all()
    return jsonify([{
        'id': review.id,
        'restaurant_id': review.restaurant_id,
        'rating': review.rating,
        'review': review.review,
        'created_at': review.created_at
    } for review in reviews])

@api.route('/restaurants/<int:id>/reviews', methods=['POST'])
def add_review(id):
    data = request.get_json()
    name = data.get('name')
    rating = data.get('rating')
    review = data.get('review')

    new_review = Review(
        restaurant_id=id,
        name=name,
        rating=rating,
        review=review
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review added successfully'}), 201
