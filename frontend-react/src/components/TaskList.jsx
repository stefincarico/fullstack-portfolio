// src/components/TaskList.jsx
import { useState, useEffect } from 'react';

const TaskList = () => {
    // 1. Stato per memorizzare i task. Inizializziamo con un array vuoto.
    const [tasks, setTasks] = useState([]);
    // (Opzionale ma consigliato) Stato per gestire il caricamento
    const [loading, setLoading] = useState(true);

    const urlApi = 'http://127.0.0.1:8000/api/v1/posts/';

    // 2. Usiamo useEffect per caricare i dati
    useEffect(() => {
        const fetchTasks = async () => {
            try {
                const response = await fetch(urlApi);
                if (!response.ok) throw new Error('Errore di rete');
                const data = await response.json();
                setTasks(data); // Salviamo i dati nello stato
            } catch (error) {
                console.error("Errore nel recupero:", error);
                // Qui potremmo impostare uno stato di errore
            } finally {
                setLoading(false); // In ogni caso, il caricamento è finito
            }
        };

        fetchTasks();
    }, []); // <-- L'array di dipendenze vuoto è FONDAMENTALE!

    // 3. Logica di rendering
    if (loading) {
        return <p>Caricamento in corso...</p>;
    }

    return (
        <ul>
            {tasks.map(task => (
                <li key={task.id}>{task.title}</li>
            ))}
        </ul>
    );
};

export default TaskList;