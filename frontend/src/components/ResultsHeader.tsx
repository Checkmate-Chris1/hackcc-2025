import styles from '../pages/ResultsPage.module.css'
import type { Results } from '../App.tsx';

interface Props {
    page: string
    setPage: ((page: ("home" | "results")) => void)
    search: string
    setSearch: ((search: string) => void)
}

export default function ResultsHeader({ page, setPage, search, setSearch }: Props) {
    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        // For demo: simply log input
        console.log("User input:", search);
        // Later: call backend to get predictions
    };

    return (
        <>
            <h1 onClick={() => setPage("home")} className="color-primary">Sitename</h1>
            <form className={styles.searchForm} onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Enter your symptoms..."
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    className={styles.searchInput}
                />
                <button type="submit" className={styles.submitButton}>Submit</button>
            </form>
        </>
    )
}