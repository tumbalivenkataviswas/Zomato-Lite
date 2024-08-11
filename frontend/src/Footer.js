import React from 'react';
import './Footer.css'; // Add your CSS file for styling

const Footer = () => {
    return (
        <footer className="footer">
            <div className="footer-content">
                <h2>Zamato</h2>
                <p>Welcome to our Zamato, your go-to platform for discovering the best restaurants around you. Explore various cuisines, check ratings, and find the perfect dining spot for any occasion.</p>
                <p>Developed with sincerity by Adari Vaibhav.</p>
                <p>Contact at: <a href="mailto:contact@zomato-clone.com">adarivaibhavmay20@gmail.com</a></p>
                <div className="social-links">
                    <a href="https://www.linkedin.com/in/vaibhav-adari-69b955250" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">🔗</a>
                    <a href="https://www.twitter.com" target="_blank" rel="noopener noreferrer" aria-label="Twitter">🐦</a>
                    <a href="https://github.com/AdariVaibhav" target="_blank" rel="noopener noreferrer" aria-label="GitHub">🐙</a>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
