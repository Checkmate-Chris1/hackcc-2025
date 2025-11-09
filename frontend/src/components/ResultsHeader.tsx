import styles from '../pages/ResultsPage.module.css'

interface Props {
    setPage: ((page: ("home" | "results")) => void)
    search: string
    setSearch: ((search: string) => void)
    fetchResults: (userInput: string) => Promise<void>
}

export default function ResultsHeader({ setPage, search, setSearch, fetchResults }: Props) {
    const handleSubmit = async () => {
        console.log("Running handleSubmit!")
        fetchResults(search)
    }

    return (
        <>
            <h1 onClick={() => setPage("home")} className="color-primary">SickAssist</h1>
            <form className={styles.searchForm} onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Enter your symptoms..."
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    className={styles.searchInput}
                />
                <button type="submit" className={styles.submitButton} onClick={handleSubmit} >Back</button>
            </form>
        </>
    )
}