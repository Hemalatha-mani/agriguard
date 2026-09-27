import { useState } from 'react'
import ChatWindow from '../components/chatbot/ChatWindow.jsx'
import ChatInput from '../components/chatbot/ChatInput.jsx'
import ErrorBanner from '../components/common/ErrorBanner.jsx'
import { sendChatMessage } from '../api/chatApi.js'

let idCounter = 0
function nextId() {
  idCounter += 1
  return idCounter
}

export default function Chatbot() {
  const [messages, setMessages] = useState([])
  const [isTyping, setIsTyping] = useState(false)
  const [error, setError] = useState('')

  async function handleSend(text) {
    setError('')
    setMessages((prev) => [...prev, { id: nextId(), role: 'user', text }])
    setIsTyping(true)

    try {
      const data = await sendChatMessage(text)
      setMessages((prev) => [...prev, { id: nextId(), role: 'bot', text: data.answer }])
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to get a response. Please try again.')
    } finally {
      setIsTyping(false)
    }
  }

  return (
    <div className="page chatbot-page">
      <h1>💬 AI Chatbot</h1>
      <p>
        Ask about crops, diseases, prevention, watering, and farming practices. For image-based
        diagnosis, use the AI Detect page instead.
      </p>

      <div className="card chatbot-container">
        <ChatWindow messages={messages} isTyping={isTyping} />
        <ErrorBanner message={error} />
        <ChatInput onSend={handleSend} disabled={isTyping} />
      </div>
    </div>
  )
}
