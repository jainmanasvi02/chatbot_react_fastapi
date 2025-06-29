// src/App.js
//import React from 'react';
import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Signup from './Signup';
import Signin from './Signin';
import Chat from './Chat';
import Main from './Main';
import ErrorBoundary from "./ErrorBoundary";

function App() {
  //const isLoggedIn = localStorage.getItem('token');
  const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem('token'));

  // When token changes, re-evaluate login status
  useEffect(() => {
    const handleStorageChange = () => {
      setIsLoggedIn(!!localStorage.getItem('token'));
    };

    window.addEventListener("storage", handleStorageChange);
    return () => window.removeEventListener("storage", handleStorageChange);
  }, []);

  return (
    <ErrorBoundary>
      <Router>
        <Routes>
          <Route path="/" element={<Main />} /> {/* ← New Main page route */}
          <Route path="/signup" element={<Signup />} />
          <Route path="/signin" element={<Signin setIsLoggedIn={setIsLoggedIn} />} />
          <Route path="/chat" element={isLoggedIn ? <Chat /> : <Navigate to="/signin" />} />
        </Routes>
      </Router>
    </ErrorBoundary>
  );
}

export default App;
