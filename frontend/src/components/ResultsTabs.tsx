import { useState } from 'react';
import styles from '../pages/ResultsPage.module.css';
import type { Results } from '../App.tsx';

export default function ResultsTabs( results: Results ) {
    const [activeTab, setActiveTab] = useState<'home' | 'conventional' | 'otc' | 'herbal'>('home');

    return (
        <div className={styles.container}>
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
                    <h1 className={styles.diseaseTitle}>{results.disease}</h1>
                    {activeTab === 'home' && <p>{results.home_remedy}</p>}
                    {activeTab === 'conventional' && <p>{results.conventional_remedy}</p>}
                    {activeTab === 'otc' && <p>{results.otc_remedy}</p>}
                    {activeTab === 'herbal' && <p>{results.herbal_remedy}</p>}
                </div>
            </div>
        </div>
    );
}
