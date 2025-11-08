import { useEffect, useState } from 'react'
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

    const messages = [
        "I haven't been feeling well...",
        "I've been having pain...",
    ];

    const [splash, setSplash] = useState("");

    useEffect(() => {
        const randomMessage = messages[Math.floor(Math.random() * messages.length)];
        setSplash(randomMessage);
    }, []);

    return (
        <>

            <div className="center-container">

                <h1>Welcome to <span className='color-primary'>Sitename</span>!</h1>

                <p className='instructions'>    
                    Write out your feelings and symptoms in the text box below, and our AI will suggest remedies.
                    <br />
                    Don't think about it too much, just write as if you're chatting to a friend.
                </p>

                <div className="input-area">

                    <textarea
                        name="symtomInput"
                        id="symtomInputBox"
                        cols={90}
                        rows={10}
                        placeholder={splash}>
                    </textarea>

                    <br />

                    <button id="submitSymtoms" onClick={sendMessage}>Submit</button>

                </div>

            </div>

        </>
    )
}

export default App
