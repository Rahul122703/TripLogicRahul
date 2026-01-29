// src/store/index.ts
import { configureStore } from "@reduxjs/toolkit";
import authReducer from "./slices/authSlice";
import tripsReducer from "./slices/tripsSlice";

export const store = configureStore({
  reducer: {
    auth: authReducer,
    trips: tripsReducer,
  },
});

// TS types
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
