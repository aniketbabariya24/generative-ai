import React, { useState } from 'react';
import './TodoApp.css';

function TodoApp() {
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [editId, setEditId] = useState(null);
  const [editValue, setEditValue] = useState('');

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleFormSubmit = (event) => {
    event.preventDefault();
    if (inputValue.trim() !== '') {
      const newTodo = {
        id: Date.now(),
        text: inputValue,
        completed: false,
        date: getCurrentDate(),
        time: getCurrentTime()
      };
      setTodos([...todos, newTodo]);
      setInputValue('');
    }
  };

  const handleTodoDelete = (todoId) => {
    const updatedTodos = todos.filter((todo) => todo.id !== todoId);
    setTodos(updatedTodos);
  };

  const handleTodoToggle = (todoId) => {
    const updatedTodos = todos.map((todo) => {
      if (todo.id === todoId) {
        return {
          ...todo,
          completed: !todo.completed
        };
      }
      return todo;
    });
    setTodos(updatedTodos);
  };

  const handleEdit = (todoId, todoText) => {
    setEditId(todoId);
    setEditValue(todoText);
  };

  const handleEditChange = (event) => {
    setEditValue(event.target.value);
  };

  const handleEditSubmit = (event, todoId) => {
    event.preventDefault();
    const updatedTodos = todos.map((todo) => {
      if (todo.id === todoId) {
        return {
          ...todo,
          text: editValue
        };
      }
      return todo;
    });
    setTodos(updatedTodos);
    setEditId(null);
    setEditValue('');
  };

  const getCurrentDate = () => {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    const currentDate = new Date().toLocaleDateString(undefined, options);
    return currentDate;
  };

  const getCurrentTime = () => {
    const options = { hour: '2-digit', minute: '2-digit' };
    const currentTime = new Date().toLocaleTimeString(undefined, options);
    return currentTime;
  };

  return (
    <div className="todo-app">
      <h1>Todo App</h1>
      <form onSubmit={handleFormSubmit}>
        <input
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          placeholder="Enter a new task"
        />
        <button type="submit">Add Task</button>
      </form>
      <table className="todo-table">
        <thead>
          <tr>
            <th>Task</th>
            <th>Date</th>
            <th>Time</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {todos.map((todo) => (
            <tr
              key={todo.id}
              className={`todo-item ${todo.completed ? 'completed' : ''}`}
            >
              <td>
                {editId === todo.id ? (
                  <form onSubmit={(e) => handleEditSubmit(e, todo.id)}>
                    <input
                      type="text"
                      value={editValue}
                      onChange={handleEditChange}
                      placeholder="Edit task"
                    />
                    <button type="submit">Save</button>
                  </form>
                ) : (
                  <span
                    className="todo-text"
                    onClick={() => handleTodoToggle(todo.id)}
                  >
                    {todo.text}
                  </span>
                )}
              </td>
              <td>{todo.date}</td>
              <td>{todo.time}</td>
              <td className="todo-actions">
                {editId !== todo.id && (
                  <>
                    <button
                      className="edit-button"
                      onClick={() => handleEdit(todo.id, todo.text)}
                    >
                      Edit
                    </button>
                    <button
                      className="delete-button"
                      onClick={() => handleTodoDelete(todo.id)}
                    >
                      Delete
                    </button>
                  </>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default TodoApp;
