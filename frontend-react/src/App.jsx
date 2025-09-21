// src/App.jsx
import { Routes, Route } from 'react-router-dom';
import TaskList from './components/TaskList';
// Creeremo questo componente tra un attimo
import TaskDetail from './components/TaskDetail'; 

function App() {
  return (
    <div className="App">
      <h1>Task Manager React</h1>
      <Routes>
        {/* Rotta per la homepage */}
        <Route path="/" element={<TaskList />} />
        
        {/* Rotta dinamica per il dettaglio */}
        <Route path="/tasks/:taskId" element={<TaskDetail />} />
      </Routes>
    </div>
  );
}
export default App;