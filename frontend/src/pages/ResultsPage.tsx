import { useState } from 'react';
import styles from './ResultsPage.module.css';

export default function ResultsPage() {
    const [activeTab, setActiveTab] = useState<'home' | 'conventional' | 'otc' | 'herbal'>('home');
    const [inputText, setInputText] = useState('');

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        // For demo: simply log input
        console.log("User input:", inputText);
        // Later: call backend to get predictions
    };

    return (
        <div className={styles.container}>
            <form className={styles.searchForm} onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Enter your symptoms..."
                    value={inputText}
                    onChange={(e) => setInputText(e.target.value)}
                    className={styles.searchInput}
                />
                <button type="submit" className={styles.submitButton}>Submit</button>
            </form>

            <div className={styles.contentWrapper}>
                <div className={styles.tabs}>
                    <button
                        className={`${styles.tabButton} ${activeTab === 'home' ? styles.active : ''}`}
                        onClick={() => setActiveTab('home')}
                    >
                        Home Remedy
                    </button>
                    <button
                        className={`${styles.tabButton} ${activeTab === 'conventional' ? styles.active : ''}`}
                        onClick={() => setActiveTab('conventional')}
                    >
                        Conventional
                    </button>
                    <button
                        className={`${styles.tabButton} ${activeTab === 'otc' ? styles.active : ''}`}
                        onClick={() => setActiveTab('otc')}
                    >
                        Over the Counter
                    </button>
                    <button
                        className={`${styles.tabButton} ${activeTab === 'herbal' ? styles.active : ''}`}
                        onClick={() => setActiveTab('herbal')}
                    >
                        Herbal
                    </button>
                </div>

                <div className={styles.tabContent}>
                    <h1 className={styles.diseaseTitle}>Common Cold</h1>
                    {activeTab === 'home' && <p>Drink warm fluids, rest, and use honey for sore throat.</p>}
                    {activeTab === 'conventional' && <p>Use decongestants, antihistamines, or see a doctor if symptoms persist.</p>}
                    {activeTab === 'otc' && <p>Acetaminophen or ibuprofen for fever and aches.</p>}
                    {activeTab === 'herbal' && <p>Ginger tea, garlic, and echinacea can help reduce symptoms.</p>}
                </div>
            </div>
        </div>
    );
}
