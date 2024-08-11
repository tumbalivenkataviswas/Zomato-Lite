import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import RestaurantList from './RestaurantList';
import RestaurantDetail from './RestaurantDetail';
import Footer from './Footer'; // Import the Footer component

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<RestaurantList />} />
                <Route path="/restaurant/:id" element={<RestaurantDetail />} />
            </Routes>
            <Footer /> {/* Include the Footer component */}
        </Router>
    );
}

export default App;
