// src/components/TaskForm.jsx
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Form, Button } from 'react-bootstrap';

// 1. Accetta `initialData`. Lo impostiamo a null di default per la modalità creazione.
const TaskForm = ({ authToken, initialData = null }) => {
    // 2. Imposta lo stato iniziale usando i dati di initialData se esistono.
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const navigate = useNavigate();

    // Questo useEffect popola il form quando i dati iniziali sono pronti
    useEffect(() => {
        if (initialData) {
            setTitle(initialData.title);
            setContent(initialData.content);
        }
    }, [initialData]); // Si attiva solo quando initialData cambia

    const handleSubmit = async (event) => {
        event.preventDefault();

        // 3. Logica condizionale per decidere se creare o aggiornare
        const isEditing = !!initialData; // true se initialData non è null

        const taskData = { title, content };
        
        // L'URL e il metodo cambiano in base alla modalità
        const url = isEditing 
            ? `http://127.0.0.1:8000/api/v1/posts/${initialData.id}/`
            : 'http://127.0.0.1:8000/api/v1/posts/';
        
        const method = isEditing ? 'PATCH' : 'POST'; // PATCH è standard per aggiornamenti parziali

        try {
            const response = await fetch(url, {
                method: method, // Usa il metodo dinamico
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authToken}`
                },
                body: JSON.stringify(taskData)
            });

            if (!response.ok) {
                const errorData = await response.json();
                console.error('Dettagli errore API:', errorData);
                throw new Error(`Errore nell'operazione: ${response.statusText}`);
            }
            
            const savedTask = await response.json();
            
            // Reindirizza alla pagina di dettaglio del task appena creato o modificato
            navigate(`/tasks/${savedTask.id}`);

        } catch (error) {
            console.error("Errore durante il submit:", error);
        }
    };

    return (
        <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3" controlId="formTaskTitle">
                <Form.Label>Titolo</Form.Label>
                <Form.Control 
                    type="text" 
                    placeholder="Inserisci il titolo"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formTaskContent">
                <Form.Label>Contenuto</Form.Label>
                <Form.Control 
                    as="textarea" 
                    rows={3}
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                />
            </Form.Group>

            {/* Cambia il testo del bottone in base alla modalità */}
            <Button variant="primary" type="submit">
                {initialData ? 'Aggiorna Task' : 'Crea Task'}
            </Button>
        </Form>
    );
};

export default TaskForm;