import axiosClient from './axiosClient.js'

export async function fetchFarmingGuide() {
  const res = await axiosClient.get('/api/farming-guide')
  return res.data
}
