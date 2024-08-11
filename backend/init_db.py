import sqlite3

def create_tables():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Create restaurants table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            address TEXT,
            cuisines TEXT,
            average_cost_for_two INTEGER,
            votes INTEGER,
            rating_text TEXT,
            aggregate_rating REAL
        )
    ''')

    # Create reviews table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurant_id INTEGER,
            name TEXT,
            rating INTEGER,
            review TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
        )
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_tables()
    print("Database initialized and tables created.")
