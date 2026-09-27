import axiosClient from './axiosClient.js'

export async function loginRequest(username, password) {
  const res = await axiosClient.post('/api/auth/login', { username, password })
  return res.data
}

export async function registerRequest(username, email, password) {
  const res = await axiosClient.post('/api/auth/register', { username, email, password })
  return res.data
}

export async function logoutRequest() {
  const res = await axiosClient.post('/api/auth/logout')
  return res.data
}

export async function fetchCurrentUser() {
  const res = await axiosClient.get('/api/auth/me')
  return res.data
}
