import React, { useState } from 'react';
import './App.css';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    const userMessage = { sender: 'You', text: input };
    setMessages((msgs) => [...msgs, userMessage]);
    setLoading(true);
    try {
      const res = await fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
      });
      const data = await res.json();
      setMessages((msgs) => [...msgs, { sender: 'Bot', text: data.response }]);
    } catch (err) {
      setMessages((msgs) => [...msgs, { sender: 'Bot', text: '[Error connecting to backend]' }]);
    }
    setInput('');
    setLoading(false);
  };

  return (
    <div className="App" style={{ maxWidth: 500, margin: '40px auto', padding: 20, background: '#f9f9f9', borderRadius: 8 }}>
      <h2>Finance & College Chatbot</h2>
      <div style={{ minHeight: 200, maxHeight: 300, overflowY: 'auto', background: '#fff', padding: 10, borderRadius: 4, marginBottom: 10, border: '1px solid #ddd' }}>
        {messages.map((msg, idx) => (
          <div key={idx} style={{ textAlign: msg.sender === 'You' ? 'right' : 'left', margin: '8px 0' }}>
            <b>{msg.sender}:</b> <span>{msg.text}</span>
          </div>
        ))}
        {loading && <div><i>Bot is typing...</i></div>}
      </div>
      <form onSubmit={sendMessage} style={{ display: 'flex', gap: 8 }}>
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Type your message..."
          style={{ flex: 1, padding: 8, borderRadius: 4, border: '1px solid #ccc' }}
          disabled={loading}
        />
        <button type="submit" disabled={loading || !input.trim()} style={{ padding: '8px 16px', borderRadius: 4, border: 'none', background: '#1976d2', color: '#fff' }}>
          Send
        </button>
      </form>
    </div>
  );
}

export default App;
