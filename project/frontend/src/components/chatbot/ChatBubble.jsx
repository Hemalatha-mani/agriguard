export default function ChatBubble({ role, text }) {
  const isUser = role === 'user'
  return (
    <div className={`chat-bubble ${isUser ? 'chat-bubble--user' : 'chat-bubble--bot'}`}>
      <span className="chat-bubble__icon">{isUser ? '🧑‍🌾' : '🤖'}</span>
      <p>{text}</p>
    </div>
  )
}
