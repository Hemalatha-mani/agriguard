import axiosClient from './axiosClient.js'

export async function fetchDashboardStats() {
  const res = await axiosClient.get('/api/dashboard')
  return res.data
}
