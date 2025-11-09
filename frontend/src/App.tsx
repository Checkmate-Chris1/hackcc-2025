import { useEffect, useState } from 'react'
import HomePage from "./pages/HomePage"
import ResultsPage from './pages/ResultsPage'
import './App.css'

export default function App() {
    const [page, setPage] = useState<"home" | "results">("home")
    const [search, setSearch] = useState<string>("")

    return (
        <>
            { page == "home" && <HomePage setPage={setPage} /> }
            { page == "results" && <ResultsPage setPage={setPage} search= /> }
        </>
    )
}
