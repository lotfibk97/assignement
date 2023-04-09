import React, { useState } from 'react';
import './App.css'; // import the CSS file
import Item from './Item.js';

function TodoList() {
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleAddTodo = () => {
    setTodos([...todos, inputValue]);
    setInputValue('');
  };

  const handleDeleteTodo = (index) => {
    const newTodos = [...todos];
    newTodos.splice(index, 1);
    setTodos(newTodos);
  };

  return (
    <div className="todo-list-container">
      <div className="todo-list-header">
        <h1 className="todo-list-title">Todo List</h1>
        <div>Total: {todos.length}</div>
      </div>
      
      <div className="todo-list-form">
        <input
          type="text"
          className="todo-list-input"
          value={inputValue}
          onChange={handleInputChange}
        />
        <button className="todo-list-add-button" onClick={handleAddTodo}>
          Add
        </button>
      </div>
      <ul className="todo-list-items">
        {todos.map((todo, index) => (
          <Item todo={todo} index={index} delete={handleDeleteTodo}></Item>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
