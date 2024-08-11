import sqlite3
import pandas as pd

data = pd.read_csv('C:\\Users\\avaib\\OneDrive\\Desktop\\zomatoFiles\\zomato.csv', encoding='latin1')  # or 'iso-8859-1' or 'cp1252'
# Renaming columns to match the database schema
data.rename(columns={
    'Restaurant ID': 'id',
    'Restaurant Name': 'name',
    'Country Code': 'country',
    'City': 'city',
    'Address': 'address',
    'Cuisines': 'cuisines',
    'Average Cost for two': 'average_cost_for_two',
    'Currency': 'currency',
    'Has Table booking': 'has_table_booking',
    'Has Online delivery': 'has_online_delivery',
    'Aggregate rating': 'aggregate_rating',
    'Rating color': 'rating_color',
    'Rating text': 'rating_text',
    'Votes': 'votes'
}, inplace=True)

# Convert boolean-like columns to 1/0
data['has_table_booking'] = data['has_table_booking'].apply(lambda x: 1 if x == 'Yes' else 0)
data['has_online_delivery'] = data['has_online_delivery'].apply(lambda x: 1 if x == 'Yes' else 0)

# Connect to SQLite database
conn = sqlite3.connect('zomato.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS restaurants (
        id INTEGER PRIMARY KEY,
        name TEXT,
        country INTEGER,
        city TEXT,
        address TEXT,
        cuisines TEXT,
        average_cost_for_two INTEGER,
        currency TEXT,
        has_table_booking BOOLEAN,
        has_online_delivery BOOLEAN,
        aggregate_rating REAL,
        rating_color TEXT,
        rating_text TEXT,
        votes INTEGER
    )
''')

# Insert data into table
data.to_sql('restaurants', conn, if_exists='replace', index=False)

conn.commit()
conn.close()
