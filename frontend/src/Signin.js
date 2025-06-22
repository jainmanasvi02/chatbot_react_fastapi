import React, { useState } from 'react';
import axios from './api';
import { useNavigate } from 'react-router-dom';

function Signin() {
  const [formData, setFormData] = useState({ username: '', password: '' });
  const navigate = useNavigate();

  const handleSignin = async (e) => {
    e.preventDefault();  // To prevent the page from reloading 
    try {
      const res = await axios.post('/signin', formData);
      localStorage.setItem('token', 'dummy_token');
      localStorage.setItem('username', res.data.username); 
      alert('Signin successful!');
      console.log("Navigating to /chat...");
      navigate('/chat');
    } catch (error) {
      console.error("Signin error:", error);
      alert('Invalid credentials');
    }
  };

  return (
    <div style={styles.body}>
      <div style={styles.container}>
        <h2 style={styles.heading}>SignIn</h2>
        <form onSubmit={handleSignin}>
          <div style={styles.inputGroup}>
            <label htmlFor="username" style={styles.label}>Email ID:</label>
            <input
              type="text"
              id="email id"
              name="email id"
              required
              value={formData.username}
              onChange={(e) => setFormData({ ...formData, username: e.target.value })}
              style={styles.input}
            />
          </div>
          <div style={styles.inputGroup}>
            <label htmlFor="password" style={styles.label}>Password:</label>
            <input
              type="password"
              id="password"
              name="password"
              required
              value={formData.password}
              onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              style={styles.input}
            />
          </div>
          <button type="submit" style={styles.button}>Signin</button>
        </form>
      </div>
    </div>
  );
}

const styles = {
  body: {
    fontFamily: 'Arial, sans-serif',
    backgroundColor: '#f4f4f4',
    margin: 0,
    padding: 0,
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    minHeight: '100vh'
  },
  container: {
    backgroundColor: '#fff',
    borderRadius: '8px',
    boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
    padding: '20px',
    width: '300px',
    textAlign: 'center'
  },
  heading: {
    marginBottom: '20px',
    color: '#333'
  },
  inputGroup: {
    marginBottom: '15px',
    textAlign: 'left'
  },
  label: {
    display: 'block',
    marginBottom: '5px',
    color: '#666'
  },
  input: {
    width: '100%',
    padding: '10px',
    border: '1px solid #ccc',
    borderRadius: '4px',
    boxSizing: 'border-box'
  },
  button: {
    backgroundColor: '#4CAF50',
    color: 'white',
    padding: '12px 20px',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    width: '100%',
    fontSize: '16px'
  }
};

export default Signin;
