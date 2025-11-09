import { useEffect, useState } from 'react'
import HomePage from "./pages/HomePage"
import ResultsPage from './pages/ResultsPage'
import './App.css'

export default function App() {
    const [page, setPage] = useState<"home" | "results">("home")
    const [search, setSearch] = useState<string>("")

    const shared = { page, setPage, search, setSearch }

    return (
        <>
            { page == "home" && <HomePage {...shared} /> }
            { page == "results" && <ResultsPage {...shared} /> }
        </>
    )
}
