// src/api/axios.ts
import axios from "axios";
import { API_BASE } from "./paths";

const api = axios.create({
  baseURL: API_BASE,
  headers: { "Content-Type": "application/json" },
  withCredentials: false, // assume token bearer header, not cookies
});

// attach token from localStorage (or window.__APP_TOKEN__) if present
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access_token");
  if (token && config.headers) {
    config.headers["Authorization"] = `Bearer ${token}`;
  }
  return config;
});

export default api;
