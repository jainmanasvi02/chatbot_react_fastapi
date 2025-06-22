import React from 'react';
import { useNavigate } from 'react-router-dom';

function Main() {
  const navigate = useNavigate();

  return (
    <div style={{ textAlign: 'center', marginTop: '150px' }}>
      <h1>Welcome to Chatbot App</h1>
      <button style={{ margin: '10px' }} onClick={() => navigate('/signup')}>Signup</button>
      <button style={{ margin: '10px' }} onClick={() => navigate('/signin')}>Signin</button>
    </div>
  );
}

export default Main;
