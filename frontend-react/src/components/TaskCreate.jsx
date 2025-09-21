// src/components/TaskCreate.jsx
import TaskForm from "./TaskForm";

// 1. Ricevi authToken come prop
const TaskCreate = ({ authToken }) => {
    return (
        <div>
            <h2>Crea un Nuovo Task</h2>
            {/* 2. Passalo a TaskForm */}
            <TaskForm authToken={authToken} />
        </div>
    );
};

export default TaskCreate;
