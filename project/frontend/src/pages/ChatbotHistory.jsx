import { useEffect, useState } from 'react'
import { fetchChatHistory, deleteChatHistoryItem } from '../api/chatApi.js'
import Loader from '../components/common/Loader.jsx'
import ErrorBanner from '../components/common/ErrorBanner.jsx'
import Card from '../components/common/Card.jsx'

export default function ChatbotHistory() {
  const [history, setHistory] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    loadHistory()
  }, [])

  function loadHistory() {
    setLoading(true)
    fetchChatHistory()
      .then(setHistory)
      .catch((err) => setError(err.response?.data?.detail || 'Failed to load chat history.'))
      .finally(() => setLoading(false))
  }

  async function handleDelete(id) {
    try {
      await deleteChatHistoryItem(id)
      setHistory((prev) => prev.filter((h) => h.id !== id))
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to delete item.')
    }
  }

  return (
    <div className="page history-page">
      <h1>🗂️ Chatbot History</h1>
      <p>All the questions you've asked the AI chatbot and its answers.</p>

      {loading && <Loader label="Loading chat history..." />}
      <ErrorBanner message={error} />

      {!loading && history.length === 0 && !error && <p>No chat history yet.</p>}

      <div className="chat-history-list">
        {history.map((item) => (
          <Card key={item.id} className="chat-history-item">
            <div className="chat-history-item__header">
              <span className="text-muted">{new Date(item.created_at).toLocaleString()}</span>
              <button
                type="button"
                className="btn btn--danger btn--small"
                onClick={() => handleDelete(item.id)}
              >
                Delete
              </button>
            </div>
            <p><strong>Q:</strong> {item.question}</p>
            <p><strong>A:</strong> {item.answer}</p>
          </Card>
        ))}
      </div>
    </div>
  )
}
