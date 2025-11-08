import { useState } from 'react'
import './App.css'

function App() {

    const [response, setResponse] = useState('')


    // USE THIS FOR GETTING AND SENDING A MESSAGE TO THE BACKEND
    const sendMessage = async () => {
        try {
            const res = await fetch("http://127.0.0.1:5000/send_message", {
                method: "POST",
            })
            const text = await res.text()
            setResponse(text)
        } catch (err) {
            console.error(err)
        }
    }
    ///////////


    return (
        <>

            <div className="center-container">

                <h1>Welcome to Sitename</h1>

                <p className='instructions'>
                    Please enter your symptoms below and click "Submit" to receive a preliminary analysis.
                </p>

                <div className="input-area">

                    <textarea
                        name="symtomInput"
                        id="symtomInputBox"
                        cols={90}
                        rows={10}
                        placeholder="Enter your text here...">
                    </textarea>

                    <br />

                    <button id="submitSymtoms" onClick={sendMessage}>Submit</button>

                </div>

            </div>

        </>
    )
}

export default App
