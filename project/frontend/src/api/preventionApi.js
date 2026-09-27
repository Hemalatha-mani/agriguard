import axiosClient from './axiosClient.js'

export async function fetchPreventionTips() {
  const res = await axiosClient.get('/api/prevention')
  return res.data
}
