# Todo List

This is a simple React application that implements a todo list. The user can add and remove items from the list.

## Technologies Used

The application is built using:

- React
- CSS

## Getting Started

1. Clone the repository:

    ```
    git clone https://github.com/lotfibk97/assignement.git
    cd qst4
    ```

2. Install dependencies:

    ```
    npm install
    ```

3. Start the application:

    ```
    npm start
    ```

4. Open http://localhost:3000 in a web browser to view the application.

## Usage

- To add an item to the list, type in the input box and click the "Add" button.

- To remove an item from the list, click the "Delete" button next to the item.

## Code Overview

The main logic for the todo list is contained in the TodoList component. This component manages the list of todos, the input value, and the logic for adding and removing todos. It also renders the Item component for each todo in the list.

The Item component is responsible for rendering an individual todo item in the list. It receives the todo text, index, and a delete function as props.
