// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Signup from './Signup';
import Signin from './Signin';
import Chat from './Chat';
import Main from './Main';

function App() {
  const isLoggedIn = localStorage.getItem('token');

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Main />} /> {/* ← New Main page route */}
        <Route path="/signup" element={<Signup />} />
        <Route path="/signin" element={<Signin />} />
        <Route path="/chat" element={isLoggedIn ? <Chat /> : <Navigate to="/signin" />} />
      </Routes>
    </Router>
  );
}

export default App;
