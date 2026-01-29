import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import { LoginPage,CallbackPage } from "./pages"

const App = () => {
  const token = localStorage.getItem("token")

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/auth/callback" element={<CallbackPage />} />

        {/* Protected route */}
        <Route
          path="/"
          element={
            token ? (
              <div className="border border-black grid place-items-center h-screen w-screen">
                FINAL FINAL div
              </div>
            ) : (
              <Navigate to="/login" />
            )
          }
        />
      </Routes>
    </BrowserRouter>
  )
}

export default App
