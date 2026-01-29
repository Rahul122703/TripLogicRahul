// src/api/paths.ts
export const API_BASE = import.meta.env.VITE_API_BASE || "https://triplogicapi-test-7c6a378ff18c.herokuapp.com";

// Update these if backend uses different paths
export const SEND_MAGIC_LINK = "/auth/magic-link/send";      // POST { email }
export const VERIFY_MAGIC_LINK = "/auth/magic-link/verify";  // POST { token } or GET ?token=...
export const ME = "/auth/me";                                // GET -> current user (expects Bearer)
export const TRIPS = "/trips";
export const TRIP = (id: string | number) => `/trips/${id}`;
export const SUPPLIERS = "/suppliers";
export const SERVICES = "/services";