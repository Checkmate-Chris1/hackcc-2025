import type { Results } from '../App.tsx';
import ResultsTabs from '../components/ResultsTabs.tsx';
import ResultsHeader from '../components/ResultsHeader.tsx';

interface Props {
    page: string
    setPage: ((page: ("home" | "results")) => void)
    search: string
    setSearch: ((search: string) => void)
    fetchResults: (userInput: string) => Promise<void>
    results: Results[]
}

export default function ResultsPage(props: Props) {
    return (
        <>
            <ResultsHeader {...props} />
            <ResultsTabs {...props.results[0]} />
            <ResultsTabs {...props.results[1]} />
            <ResultsTabs {...props.results[2]} />
        </>
    )
}