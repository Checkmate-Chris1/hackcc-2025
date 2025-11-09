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

    const results_demo: Results = {
        disease: "Influenza (Flu)",
        home_remedy: "Get plenty of rest and stay hydrated. Warm fluids like soup and tea can help soothe your throat and loosen congestion.",
        conventional_remedy: "Doctors may prescribe antiviral medications such as oseltamivir (Tamiflu) or zanamivir (Relenza) to shorten the duration and severity of the flu.",
        otc_remedy: "Over-the-counter medicines like acetaminophen (Tylenol) or ibuprofen (Advil) can reduce fever and body aches, while cough suppressants and decongestants can ease symptoms.",
        herbal_remedy: "Elderberry syrup, echinacea, and ginger tea are traditional herbal supports believed to strengthen immune response and ease flu symptoms."
    };
    const results_demo2: Results = {
        disease: "Common Cold",
        home_remedy: "Drink plenty of fluids and get rest.",
        conventional_remedy: "Use decongestants or antihistamines as prescribed.",
        otc_remedy: "Try over-the-counter cold medications like DayQuil or NyQuil.",
        herbal_remedy: "Ginger tea and honey can help soothe sore throats."
  };

    const shared = { page, setPage, search, setSearch }

    return (
        <>
            {page == "home" && <HomePage {...shared} />}
            {page == "results" && <ResultsPage {...shared} results={[results_demo, results_demo2, results_demo]} /> }
        </>
    )
}
