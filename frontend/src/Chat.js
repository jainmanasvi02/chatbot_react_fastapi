import React, { useState, useEffect } from 'react'; //react inbuilt function to call hooks(typewriter function in my code)
import { useNavigate } from 'react-router-dom';
import axios from './api';
import './App.css';
import useTypewriter from './hooks/useTypewriter'; //the typewriter function we saved inside hooks folder
import ReactMarkdown from 'react-markdown';


export default function Chat() {
  console.log("Chat rendered");
  const [userInput, setUserInput] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const navigate = useNavigate();

  const [loading, setLoading] = useState(true);

  useEffect(() => {   
    const token = localStorage.getItem('token');
    const email = localStorage.getItem('email');
    console.log("EMAIL:", email, "TOKEN:", token);

    if (!token || !email) {
      navigate('/signin');
      return;
    }

    // get chat history
    axios.get(`/history/${email}`)
      .then(res => {
        const history = res.data.map(msg => ({
          sender: 'user',
          text: msg
        }));
        setChatHistory(history);
      })
      .catch(err => console.error('Error fetching history:', err))
      .finally(() => setLoading(false));
  }, [navigate]);

  if (loading) return <div>Loading chat...</div>;

  const sendMessage = async () => {
    if (!userInput.trim()) return;

    const email = localStorage.getItem('email');
    const token = localStorage.getItem('token');
    const userMessage = { sender: 'user', text: userInput };
    setChatHistory(prev => [...prev, userMessage]);

    try {
      const response = await axios.post(
        '/chat',
        { content: userInput, email },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      const botMessage = {
        sender: 'bot',
        text: response.data.bot_response || response.data.response,
      };

      setChatHistory(prev => [...prev, botMessage]);
    } catch (error) {
      const botMessage = { sender: 'bot', text: 'Error getting response' };
      setChatHistory(prev => [...prev, botMessage]);
      console.error('Error:', error);
    }

    setUserInput('');
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('email');
    navigate('/signin');
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h2>Chatbot</h2>
        <button onClick={handleLogout} className="logout-btn">Logout</button>
      </div>

      <div className="chat-box">
        {chatHistory.map((msg, idx) => (
          <ChatMessage key={idx} message={msg.text} sender={msg.sender} />
        ))}
      </div>

      <div className="input-area">
        <input
          type="text"
          value={userInput}
          onChange={e => setUserInput(e.target.value)}
          onKeyDown={e => {
            if (e.key === 'Enter') {
              sendMessage();
            }
          }}
          placeholder="Type your message..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

function ChatMessage({ message, sender }) {
  const typedText = useTypewriter(message, 20); //typewriter effect

  return (
    
    <div className={sender}>
        {sender === 'bot' ? (
        <ReactMarkdown>{typedText}</ReactMarkdown> //markdown is for getting formatted document and not just plain text
      ) : (
        <span>{message}</span>
      )}
    </div>
  );
}
