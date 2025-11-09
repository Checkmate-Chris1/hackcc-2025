import { useEffect, useState } from 'react'

interface Props {
    page: string
    setPage: ((page: ("home" | "results")) => void)
    search: string
    setSearch: ((search: string) => void)
    fetchResults: (userInput: string) => Promise<void>
}

export default function HomePage( {page, setPage, search, setSearch, fetchResults }: Props ) {
    const handleSubmit = async () => {
        console.log("Running handleSubmit!")
        fetchResults(search)
        const submitButton = document.getElementById("submitSymtoms") as HTMLButtonElement | null;
        if (submitButton) {
            submitButton.disabled = true;
            submitButton.innerHTML = '<div class="loading-dots"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>';
        }
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

                <h1>Welcome to <span className='color-primary'>SickAssist</span>!</h1>

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
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                        placeholder={splash}>
                    </textarea>

                    <br />

                    <button id="submitSymtoms" onClick={handleSubmit}>Submit</button>

                </div>

            </div>

        </>
    )
}