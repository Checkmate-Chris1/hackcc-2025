import { useState } from 'react'
import HomePage from "./pages/HomePage"
import ResultsPage from './pages/ResultsPage.tsx'
import './App.css'

export interface Results {
    disease: string
    home_remedy: string
    conventional_remedy: string
    otc_remedy: string
    herbal_remedy: string
}

export default function App() {
    const [page, setPage] = useState<"home" | "results">("home")
    const [search, setSearch] = useState<string>("")
    const [results, setResults] = useState<Results[]>([])

    const fetchResults = async (userInput: string) => {
        try {
            const rawResponse = await fetch("http://127.0.0.1:5000/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userInput }),
            });

            const data: Results[] = await rawResponse.json(); // Expecting a list of 3 Results objects

            // Set the state directly with the returned array
            setResults(data); 
            setPage("results"); // navigate to results page
        } catch (err) {
            console.error("Error fetching results:", err);
        }
    };


    const shared = { page, setPage, search, setSearch, fetchResults }

    return (
        <>
            {page == "home" && <HomePage {...shared} />}
            {page == "results" && <ResultsPage {...shared} results={results} /> }
        </>
    )
}
