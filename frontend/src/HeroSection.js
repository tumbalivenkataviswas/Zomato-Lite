import React, { useState } from 'react';
import './HeroSection.css';

const HeroSection = ({ onSearch }) => {
    const [searchTerm, setSearchTerm] = useState('');

    const handleInputChange = (e) => {
        setSearchTerm(e.target.value);
    };

    const handleSearch = () => {
        onSearch(searchTerm);
    };

    return (
        <div className="hero-section">
            <h1>Welcome to Zamato</h1>
            <p>Discover the best restaurants around you</p>
            <div className="search-bar-container">
                <div className="search-bar">
                    <input
                        type="text"
                        placeholder="Search for restaurants..."
                        value={searchTerm}
                        onChange={handleInputChange}
                    />
                    <button onClick={handleSearch}>Search</button>
                </div>
            </div>
        </div>
    );
};

export default HeroSection;