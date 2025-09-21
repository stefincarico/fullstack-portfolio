// frontend-vanilla/app.js

// 1. Selezioniamo gli elementi del DOM con cui interagiremo
const listaTaskUl = document.querySelector('#lista-task');
const urlApi = 'http://127.0.0.1:8000/api/v1/posts/'; // Useremo i post come task

// 2. Funzione per renderizzare i task nel DOM
const renderTasks = (tasks) => {
    listaTaskUl.innerHTML = ''; // Svuotiamo la lista prima di riempirla
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = task.title;
        li.dataset.id = task.id; // Aggiungiamo l'ID per usi futuri
        listaTaskUl.appendChild(li);
    });
};

// 3. Funzione asincrona per recuperare i task dall'API
const fetchTasks = async () => {
    try {
        const response = await fetch(urlApi);
        if (!response.ok) throw new Error('Errore di rete');
        const tasks = await response.json();
        renderTasks(tasks);
    } catch (error) {
        console.error("Errore nel recuperare i task:", error);
        listaTaskUl.innerHTML = '<li>Impossibile caricare i task.</li>';
    }
};

// 4. Eseguiamo la funzione quando lo script viene caricato
fetchTasks();

// ... (codice precedente) ...

// 5. Selezioniamo il form e l'input
const formNuovoTask = document.querySelector('#form-nuovo-task');
const inputTitoloTask = document.querySelector('#input-titolo-task');

// 6. Funzione per gestire l'invio del form
const handleFormSubmit = async (event) => {
    event.preventDefault(); // Impedisce al browser di ricaricare la pagina

    const titolo = inputTitoloTask.value.trim();
    if (!titolo) return; // Non inviare se l'input è vuoto

    const nuovoTask = {
        title: titolo,
        content: 'Contenuto di default' // Il nostro modello richiede un contenuto
    };

    const authToken ='QUI-IL-TOKEN'

    try {
        // Per inviare dati, dobbiamo autenticarci! Per ora, bypasseremo
        // temporaneamente i permessi per fare il test.
        
        const response = await fetch(urlApi, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${authToken}`
            },
            body: JSON.stringify(nuovoTask),
        });

        if (!response.ok) {
            const errorData = await response.json();
            console.error('Dettagli errore:', errorData);
            throw new Error('Errore nella creazione');
        }
        
        // Se la creazione va a buon fine, ricarichiamo la lista
        fetchTasks();
        inputTitoloTask.value = ''; // Svuotiamo l'input
    } catch (error) {
        console.error("Errore nella creazione del task:", error);
        alert("Errore: impossibile creare il task.");
    }
};

// 7. Aggiungiamo l'event listener al form
formNuovoTask.addEventListener('submit', handleFormSubmit);

// 4. Eseguiamo la funzione quando lo script viene caricato
fetchTasks();