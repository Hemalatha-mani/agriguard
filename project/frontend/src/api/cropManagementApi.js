import axiosClient from './axiosClient.js'

export async function fetchCropManagementList() {
  const res = await axiosClient.get('/api/crop-management')
  return res.data
}

export async function fetchCropManagementByName(cropName) {
  const res = await axiosClient.get(`/api/crop-management/${cropName}`)
  return res.data
}
