import React from 'react';
import CVUploader from './components/CVUploader';
import './App.css';
import { FaGithub } from 'react-icons/fa'; // Import ikon

function App() {
  return (
    <div className="App">
      <nav className="navbar">
        <div className="logo">Aksara Global</div>
        <div className="nav-links">
          <a href="#home">Home</a>
          <a href="#about">About</a>
          <a href="https://github.com" target="_blank" rel="noopener noreferrer">
            <FaGithub size={24} />
          </a>
        </div>
      </nav>

      <main className="content">
        <CVUploader />
      </main>

      <footer className="footer">
        <p>&copy; 2025 Aksara Global. All Rights Reserved. Empowering Careers with AI.</p>
      </footer>
    </div>
  );
}

export default App;