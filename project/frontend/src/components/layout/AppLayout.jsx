import { useState } from 'react'
import { Outlet } from 'react-router-dom'
import Sidebar from './Sidebar.jsx'

export default function AppLayout() {
  const [sidebarOpen, setSidebarOpen] = useState(false)

  return (
    <div className="app-shell">
      <Sidebar isOpen={sidebarOpen} onClose={() => setSidebarOpen(false)} />

      <div className="app-shell__main">
        <header className="app-shell__topbar">
          <button
            className="app-shell__menu-btn"
            onClick={() => setSidebarOpen(true)}
            aria-label="Open menu"
            type="button"
          >
            ☰
          </button>
          <span className="app-shell__topbar-title">AgriGuard</span>
        </header>

        <main className="app-shell__content">
          <Outlet />
        </main>
      </div>
    </div>
  )
}
