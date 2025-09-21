// src/components/TaskDetail.jsx
import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';

const TaskDetail = () => {
    const [task, setTask] = useState(null);
    const [loading, setLoading] = useState(true);
    const { taskId } = useParams(); // Legge il parametro :taskId dall'URL

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
    }, [taskId]); // Riesegui l'effetto se l'ID del task cambia

    if (loading) return <p>Caricamento...</p>;
    if (!task) return <p>Task non trovato.</p>;

    return (
        <div>
            <h2>{task.title}</h2>
            <p>{task.content}</p>
              <p>
                {new Date(task.created_at).toLocaleString('it-IT', {
                dateStyle: 'full',
                timeStyle: 'short',
                })}
            </p>
            <p><small>Autore: {task.author_username}</small></p>
            <Link to={`/tasks/${task.id}/edit`}>Modifica Task</Link>
            {' | '}
            <Link to="/">Torna alla lista</Link>
        </div>
    );
};

export default TaskDetail;