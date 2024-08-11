from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String, nullable=False)
    country_code = db.Column(db.BigInteger, nullable=False)
    city = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    locality = db.Column(db.String, nullable=False)
    locality_verbose = db.Column(db.String, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    cuisines = db.Column(db.String, nullable=False)
    average_cost_for_two = db.Column(db.BigInteger, nullable=False)
    currency = db.Column(db.String, nullable=False)
    has_table_booking = db.Column(db.String, nullable=False)
    has_online_delivery = db.Column(db.String, nullable=False)
    is_delivering_now = db.Column(db.String, nullable=False)
    switch_to_order_menu = db.Column(db.String, nullable=False)
    price_range = db.Column(db.BigInteger, nullable=False)
    aggregate_rating = db.Column(db.Float, nullable=False)
    rating_color = db.Column(db.String, nullable=False)
    rating_text = db.Column(db.String, nullable=False)
    votes = db.Column(db.BigInteger, nullable=False)
    reviews = db.relationship('Review', backref='restaurant', lazy=True)

class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.BigInteger, db.ForeignKey('restaurants.id'), nullable=False)
    name = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
