import React from 'react';
import './Item.css';

function Item(props) {


  return (
    <div className="todo-list-form">
        <li key={props.index} className="todo-list-item">
          <p className="todoListText">  {props.todo}</p>
            <button onClick={() => props.delete(props.index)}>Delete</button>
        </li>
    </div>
  );
}

export default Item;
