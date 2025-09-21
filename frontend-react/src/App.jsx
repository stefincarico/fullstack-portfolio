// src/App.jsx
import { useState } from 'react';
import { Routes, Route } from 'react-router-dom';
import TaskList from './components/TaskList';
import Layout from './components/Layout';
import TaskDetail from './components/TaskDetail'; 
import TaskCreate from './components/TaskCreate';
import TaskEdit from './components/TaskEdit'; // <-- 1. IMPORTA IL NUOVO COMPONENTE

function App() {
  const [token, _setToken] = useState('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4NDc0NjI3LCJpYXQiOjE3NTg0NzQzMjcsImp0aSI6Ijc3NDZjNzU0ODAzMzQ2ZTFiMGZlYTdkMjJkZGIyNTY4IiwidXNlcl9pZCI6IjIifQ.x2TL4uHIC9DGigZu7aSJyRRaUFlm9RpT_utIPuYR4ys');

  return (
    <div className="App">
    <Routes>
    <Route path="/" element={<Layout />}>
        <Route index element={<TaskList />} />
        <Route path="tasks/new" element={<TaskCreate authToken={token} />} />
        <Route path="tasks/:taskId" element={<TaskDetail />} />
        {/* 2. AGGIUNGI LA NUOVA ROTTA E PASSA IL TOKEN */}
        <Route path="tasks/:taskId/edit" element={<TaskEdit authToken={token} />} />
    </Route>
    </Routes>
    </div>
  );
}
export default App;