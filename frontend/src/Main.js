import React from 'react';
import { useNavigate } from 'react-router-dom';
import './App.css';

function Main() {
  const navigate = useNavigate();

  /*return (
    <div style={{ textAlign: 'center', marginTop: '150px' }}>
      <h1>Welcome to Chatbot App</h1>
      <button style={{ margin: '10px' }} onClick={() => navigate('/signup')}>Signup</button>
      <button style={{ margin: '10px' }} onClick={() => navigate('/signin')}>Signin</button>
    </div>
  );
}*/


    /*return (
        <div className="main-landing">
          <div className="main-box">
            <h1 className="main-heading">🤖 Welcome to AI Chatbot</h1>
            <p className="main-subtitle">Your personal assistant powered by AI</p>
            <div className="main-buttons">
              <button className="main-btn" onClick={() => navigate('/signup')}>Signup</button>
              <button className="main-btn outline" onClick={() => navigate('/signin')}>Signin</button>
            </div>
          </div>
          
      </div>
    );*/

    return (
      <div className="main-bg-wrapper">
        <div className="main-bg-shape"></div>
        <div className="main-bg-shape second-shape"></div>
    
        <div className="main-landing">
          <div className="main-box">
            <h1 className="main-heading">🤖 Welcome to AI Chatbot</h1>
            <p className="main-subtitle">Your personal assistant powered by AI</p>
            <div className="main-buttons">
              <button className="main-btn" onClick={() => navigate('/signup')}>Signup</button>
              <button className="main-btn outline" onClick={() => navigate('/signin')}>Signin</button>
            </div>
          </div>
        </div>
      </div>
    );
    
  }

export default Main;
