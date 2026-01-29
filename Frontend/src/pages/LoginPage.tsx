import { useState } from "react"

const LoginPage = () => {
  const [email, setEmail] = useState("")
  const [sent, setSent] = useState(false)
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)

    try {
      const res = await fetch("http://localhost:8000/auth/magic-link", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email }),
      })

      if (!res.ok) throw new Error("Failed")

      setSent(true)
    } catch {
      alert("Failed to send magic link")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="h-screen grid place-items-center">
      <div className="border p-6 w-[350px]">
        {sent ? (
          <p>Magic link sent to your email. Check inbox.</p>
        ) : (
          <form onSubmit={handleSubmit} className="flex flex-col gap-4">
            <h2 className="text-lg font-bold">Login</h2>

            <input
              type="email"
              placeholder="Enter email"
              className="border p-2"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />

            <button
              disabled={loading}
              className="border bg-black text-white p-2"
            >
              {loading ? "Sending..." : "Send Magic Link"}
            </button>
          </form>
        )}
      </div>
    </div>
  )
}

export default LoginPage
