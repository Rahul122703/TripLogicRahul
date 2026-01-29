// src/pages/Login.tsx
import { useState  } from "react";
import type { FormEvent ,ChangeEvent} from "react";

const LoginPage = () => {
  const [email, setEmail] = useState<string>("");
  const [sent, setSent] = useState<boolean>(false);

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const res = await fetch("http://localhost:8000/auth/send-magic-link", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });

      if (!res.ok) {
        const txt = await res.text();
        throw new Error(txt || "Failed to send link");
      }

      setSent(true);
    } catch (err) {
      const message =
        err instanceof Error ? err.message : "Something went wrong";
      alert("Error: " + message);
    }
  };

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setEmail(e.target.value);
  };

  return (
    <div>
      <h2>Login</h2>

      {!sent ? (
        <form onSubmit={handleSubmit}>
          <input
            type="email"
            value={email}
            onChange={handleChange}
            placeholder="you@yourcompany.com"
            required
          />
          <button type="submit">Send magic link</button>
        </form>
      ) : (
        <p>Link sent. Check your email.</p>
      )}
    </div>
  );
};

export default LoginPage;
