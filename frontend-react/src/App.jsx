// src/App.jsx
import { Routes, Route } from 'react-router-dom';
import TaskList from './components/TaskList';
import Layout from './components/Layout'; // <-- IMPORTA IL LAYOUT
// Creeremo questo componente tra un attimo
import TaskDetail from './components/TaskDetail'; 

function App() {
  return (
    <div className="App">
    <Routes>
      <Route path="/" element={<Layout />}>
        {/* Queste rotte verranno renderizzate dove si trova l'Outlet */}
        <Route index element={<TaskList />} /> 
        <Route path="tasks/:taskId" element={<TaskDetail />} />
      </Route>
    </Routes>
    </div>
  );
}
export default App;