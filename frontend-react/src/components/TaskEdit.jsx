// src/components/TaskEdit.jsx
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import TaskForm from './TaskForm';

const TaskEdit = ({ authToken }) => {
    const [task, setTask] = useState(null);
    const [loading, setLoading] = useState(true);
    const { taskId } = useParams(); // 1. Legge l'ID dall'URL

    // 2. Carica i dati del task da modificare
    useEffect(() => {
        const fetchTask = async () => {
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/posts/${taskId}/`);
                if (!response.ok) throw new Error('Task non trovato');
                const data = await response.json();
                setTask(data);
            } catch (error) {
                console.error("Errore:", error);
            } finally {
                setLoading(false);
            }
        };
        fetchTask();
    }, [taskId]);

    // Mostra un messaggio di caricamento mentre aspettiamo i dati
    if (loading) {
        return <p>Caricamento dati del task...</p>;
    }

    // 3. Una volta caricati, passa i dati al form
    return (
        <div>
            <h2>Modifica Task</h2>
            <TaskForm initialData={task} authToken={authToken} />
        </div>
    );
};

export default TaskEdit;
