import { useEffect, useState } from 'react'

interface Props {
    setPage: ((page: ("home" | "results")) => void)
}

export default function HomePage( {setPage}: Props ) {
    const sendMessage = async () => {
        const response = await fetch('http://127.0.0.1:5000/send_message', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: 'Hello from React button!' }),
        })
        console.log("Client received response: ", response)
    }

    const messages = [
        "I haven't been feeling well...",
        "There's been this thing...",
        "I've been having pain...",
        "Well, for starters...",
        "Lately, I've noticed...",
        "It's been hard to explain...",
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
                    Write out your feelings and symptoms in the text box below, and our proprietary predictive model will suggest remedies.
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

                    <button id="submitSymtoms" onClick={() => setPage("results")}>Submit</button>

                </div>

            </div>

        </>
    )
}