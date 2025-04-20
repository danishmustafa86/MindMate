import { useState } from 'react'
import './App.css'

function App() {
  const [mood, setMood] = useState("")
  const [entry, setEntry] = useState("")
  const [response, setResponse] = useState("")

  const handleAnalyze = async () => {
    try {
      const res = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mood, entry })
      })
      const data = await res.json()
      setResponse(data.analysis)
    } catch {
      setResponse("Error: Could not reach server.")
    }
  }

  return (
    <div style={{ maxWidth: 600, margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h1>MindMate 🧠</h1>
      <input
        style={{ width: '100%', padding: '0.5rem', margin: '0.5rem 0' }}
        placeholder="How do you feel?"
        value={mood}
        onChange={e => setMood(e.target.value)}
      />
      <textarea
        style={{ width: '100%', padding: '0.5rem', height: '150px' }}
        placeholder="Write your thoughts..."
        value={entry}
        onChange={e => setEntry(e.target.value)}
      />
      <button
        style={{ padding: '0.75rem 1.5rem', marginTop: '1rem', cursor: 'pointer' }}
        onClick={handleAnalyze}
      >
        Analyze
      </button>
      {response && (
        <div style={{
          marginTop: '1.5rem',
          padding: '1rem',
          border: '1px solid #ddd',
          borderRadius: '8px'
        }}>
          <strong>AI Response:</strong>
          <p>{response}</p>
        </div>
      )}
    </div>
  )
}

export default App
