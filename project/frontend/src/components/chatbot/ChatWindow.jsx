import { useEffect, useRef } from 'react'
import ChatBubble from './ChatBubble.jsx'

export default function ChatWindow({ messages, isTyping }) {
  const endRef = useRef(null)

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, isTyping])

  return (
    <div className="chat-window">
      {messages.length === 0 && (
        <p className="chat-window__empty">
          👋 Ask me anything about crops, diseases, prevention, or farming practices.
        </p>
      )}
      {messages.map((m) => (
        <ChatBubble key={m.id} role={m.role} text={m.text} />
      ))}
      {isTyping && <ChatBubble role="bot" text="Typing..." />}
      <div ref={endRef} />
    </div>
  )
}
