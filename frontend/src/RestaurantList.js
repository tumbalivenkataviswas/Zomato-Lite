import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import Slider from 'react-slick';
import HeroSection from './HeroSection';
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";
import './RestaurantList.css';

const RestaurantList = () => {
    const [restaurants, setRestaurants] = useState([]);
    const [error, setError] = useState(null);

    const fetchRestaurants = async (searchTerm = '') => {
        try {
            const response = await axios.get(`http://localhost:5008/restaurants?search=${searchTerm}&page=1`);
            if (response.data && Array.isArray(response.data.restaurants)) {
                setRestaurants(response.data.restaurants);
            } else if (Array.isArray(response.data)) {
                setRestaurants(response.data);
            } else {
                setError('Unexpected response structure');
            }
        } catch (error) {
            setError('Error fetching data');
        }
    };

    useEffect(() => {
        fetchRestaurants();
    }, []);

    const handleSearch = (searchTerm) => {
        fetchRestaurants(searchTerm);
    };

    const settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
    };

    // Define color classes based on the rating text
    const getColorClass = (ratingText) => {
        switch (ratingText) {
            case 'Excellent':
                return 'green-dark';
            case 'Very Good':
                return 'green';
            case 'Good':
                return 'yellow';
            case 'Average':
                return 'orange';
            case 'Not Rated':
            default:
                return 'white';
        }
    };

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div>
            <HeroSection onSearch={handleSearch} />
            <div className="restaurant-list">
                {restaurants.length > 0 ? (
                    <Slider {...settings}>
                        {restaurants.map((restaurant) => (
                            <div 
                                className={`restaurant-card ${getColorClass(restaurant.rating_text)}`} 
                                key={restaurant.id}
                            >
                                <Link to={`/restaurant/${restaurant.id}`}>
                                    <h1>{restaurant.name}</h1>
                                    <div className="restaurant-info">
                                        <h2>Rating: {restaurant.aggregate_rating}</h2>
                                        <h3>Cuisines: {restaurant.cuisines}</h3>
                                    </div>
                                </Link>
                            </div>
                        ))}
                    </Slider>
                ) : (
                    <p>No restaurants found</p>
                )}
            </div>
        </div>
    );
};

export default RestaurantList;
