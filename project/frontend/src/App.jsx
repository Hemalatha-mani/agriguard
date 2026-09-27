import { Routes, Route } from 'react-router-dom'
import ProtectedRoute from './components/layout/ProtectedRoute.jsx'
import AppLayout from './components/layout/AppLayout.jsx'

import Login from './pages/Login.jsx'
import Home from './pages/Home.jsx'
import AIDetect from './pages/AIDetect.jsx'
import Diseases from './pages/Diseases.jsx'
import Remedies from './pages/Remedies.jsx'
import Prevention from './pages/Prevention.jsx'
import FarmingGuide from './pages/FarmingGuide.jsx'
import CropManagement from './pages/CropManagement.jsx'
import Chatbot from './pages/Chatbot.jsx'
import PredictionHistory from './pages/PredictionHistory.jsx'
import ChatbotHistory from './pages/ChatbotHistory.jsx'
import NotFound from './pages/NotFound.jsx'

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />

      <Route element={<ProtectedRoute />}>
        <Route element={<AppLayout />}>
          <Route path="/" element={<Home />} />
          <Route path="/ai-detect" element={<AIDetect />} />
          <Route path="/diseases" element={<Diseases />} />
          <Route path="/remedies" element={<Remedies />} />
          <Route path="/prevention" element={<Prevention />} />
          <Route path="/farming-guide" element={<FarmingGuide />} />
          <Route path="/crop-management" element={<CropManagement />} />
          <Route path="/chatbot" element={<Chatbot />} />
          <Route path="/prediction-history" element={<PredictionHistory />} />
          <Route path="/chatbot-history" element={<ChatbotHistory />} />
        </Route>
      </Route>

      <Route path="*" element={<NotFound />} />
    </Routes>
  )
}
