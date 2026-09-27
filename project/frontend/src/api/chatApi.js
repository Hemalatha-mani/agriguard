import axiosClient from './axiosClient.js'

export async function sendChatMessage(message) {
  const res = await axiosClient.post('/api/chat', { message })
  return res.data
}

export async function fetchChatHistory() {
  const res = await axiosClient.get('/api/chat-history')
  return res.data
}

export async function deleteChatHistoryItem(id) {
  const res = await axiosClient.delete(`/api/chat-history/${id}`)
  return res.data
}
