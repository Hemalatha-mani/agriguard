import { NavLink } from 'react-router-dom'
import LogoutButton from './LogoutButton.jsx'

const NAV_ITEMS = [
  { to: '/', label: 'Home', icon: '🏠' },
  { to: '/ai-detect', label: 'AI Detect', icon: '🔬' },
  { to: '/diseases', label: 'Diseases', icon: '🦠' },
  { to: '/remedies', label: 'Remedies', icon: '💊' },
  { to: '/prevention', label: 'Prevention', icon: '🛡️' },
  { to: '/farming-guide', label: 'Farming Guide', icon: '📖' },
  { to: '/crop-management', label: 'Crop Management', icon: '🌾' },
  { to: '/chatbot', label: 'AI Chatbot', icon: '💬' },
  { to: '/prediction-history', label: 'Prediction History', icon: '📊' },
  { to: '/chatbot-history', label: 'Chatbot History', icon: '🗂️' },
]

export default function Sidebar({ isOpen, onClose }) {
  return (
    <>
      <aside className={`sidebar ${isOpen ? 'sidebar--open' : ''}`}>
        <div className="sidebar__brand">
          <span className="sidebar__brand-icon">🌱</span>
          <span className="sidebar__brand-name">AgriGuard</span>
        </div>

        <nav className="sidebar__nav">
          {NAV_ITEMS.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.to === '/'}
              onClick={onClose}
              className={({ isActive }) =>
                `sidebar__link ${isActive ? 'sidebar__link--active' : ''}`
              }
            >
              <span className="sidebar__link-icon">{item.icon}</span>
              <span>{item.label}</span>
            </NavLink>
          ))}
        </nav>

        <div className="sidebar__footer">
          <LogoutButton />
        </div>
      </aside>

      {isOpen && <div className="sidebar__overlay" onClick={onClose} />}
    </>
  )
}
