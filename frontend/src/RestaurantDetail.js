import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import './RestaurantDetail.css';

const RestaurantDetail = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [restaurant, setRestaurant] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [reviews, setReviews] = useState([]);
    const [newReview, setNewReview] = useState({ name: '', rating: '', review: '' });

    useEffect(() => {
        const fetchRestaurant = async () => {
            try {
                const response = await axios.get(`http://localhost:5008/restaurants/${id}`);
                setRestaurant(response.data);
                setLoading(false);
            } catch (error) {
                setError(error);
                setLoading(false);
            }
        };

        const fetchReviews = async () => {
            try {
                const response = await axios.get(`http://localhost:5008/restaurants/${id}/reviews`);
                setReviews(response.data);
            } catch (error) {
                setError(error);
            }
        };

        fetchRestaurant();
        fetchReviews();
    }, [id]);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNewReview((prevReview) => ({ ...prevReview, [name]: value }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post(`http://localhost:5008/restaurants/${id}/reviews`, newReview);
            const response = await axios.get(`http://localhost:5008/restaurants/${id}/reviews`);
            setReviews(response.data);
            setNewReview({ name: '', rating: '', review: '' });
        } catch (error) {
            setError(error);
            console.error('Error submitting review:', error);
        }
    };    

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;

    return (
        <div className="restaurant-detail">
            <h1>{restaurant.name}</h1>
            <div className="details-container">
                <p><span className="info-label">Address:</span> {restaurant.address}</p>
                <p><span className="info-label">Cuisines:</span> {restaurant.cuisines}</p>
                <p><span className="info-label">Average Cost for Two:</span> {restaurant.average_cost_for_two}</p>
                <p><span className="info-label">Votes:</span> {restaurant.votes}</p>
                <p><span className="info-label">Rating (Avg):</span> {restaurant.aggregate_rating}</p>
            </div>

            <h2>Reviews</h2>
            <ul>
                {reviews.map((review) => (
                    <li key={review.id}>
                        <p><strong>Name:</strong> {review.name}</p> {/* Add this line */}
                        <p><strong>Rating:</strong> {review.rating}</p>
                        <p>{review.review}</p>
                    </li>
                ))}
            </ul>

            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="name">Name: </label> {/* Add this block */}
                    <input
                        type="text"
                        id="name"
                        name="name"
                        value={newReview.name}
                        onChange={handleInputChange}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="rating">Rating: </label>
                    <input
                        type="number"
                        id="rating"
                        name="rating"
                        value={newReview.rating}
                        onChange={handleInputChange}
                        required
                        min="1"
                        max="5"
                    />
                </div>
                <div>
                    <label htmlFor="review">Review: </label>
                    <textarea
                        id="review"
                        name="review"
                        value={newReview.review}
                        onChange={handleInputChange}
                        required
                    />
                </div>
                <button type="submit">Add Review</button>
            </form>

            <button onClick={() => navigate(-1)}>Back to list</button>
        </div>
    );
};

export default RestaurantDetail;
