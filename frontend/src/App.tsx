import { useState } from "react"
import reactLogo from "./assets/react.svg"
import viteLogo from "/vite.svg"
import "./App.css"

function App() {
  const [input, setInput] = useState("")      // textbox value
  const [response, setResponse] = useState("") // backend response

  const sendMessage = async () => {
    try {
      const res = await fetch("http://127.0.0.1:5000/send_message", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }), // send textbox value
      })
      const text = await res.text()
      setResponse(text)
    } catch (err) {
      console.error(err)
      setResponse("Error sending message")
    }
  }

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>

      <h1>Vite + React</h1>

      <div className="card">
        {/* Textbox for input */}
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
        />

        {/* Send button */}
        <button onClick={sendMessage}>Send Message</button>

        {/* Backend response */}
        <p>{response}</p>

        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>

      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
