import { useEffect } from "react"
import { useNavigate } from "react-router-dom"

const CallbackPage = () => {
  const navigate = useNavigate()

  useEffect(() => {
    const params = new URLSearchParams(window.location.search)
    const token = params.get("token")

    if (!token) {
      alert("No token found")
      return
    }

    const verify = async () => {
      try {
        const res = await fetch("http://localhost:8000/auth/verify", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ token }),
        })

        if (!res.ok) throw new Error("Invalid token")

        const data = await res.json()

        // Save JWT from backend
        localStorage.setItem("token", data.access_token)

        // Redirect to app
        navigate("/")
      } catch {
        alert("Login failed or link expired")
      }
    }

    verify()
  }, [navigate])

  return (
    <div className="h-screen grid place-items-center">
      Verifying magic link...
    </div>
  )
}

export default CallbackPage
