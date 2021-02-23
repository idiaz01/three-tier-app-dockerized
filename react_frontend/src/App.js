import React, { Component } from 'react';
import axios from 'axios';

import './App.css';

const apiUrl = 'http://localhost:5000/api';

class App extends Component {
  state = {
    todos: []
  };

  async getTodos() {
    const res = await axios.get(apiUrl);
    this.setState({
      todos: res.data
    })
  }
  render() {
    return (
      <div className="App">
        <h1>This is a test webapp</h1>
        <h2>I will read the data from Flask API connected to MongoDB: </h2>
        <button onClick={() => this.getTodos()}>Get data</button>
        <h2>Todo list: </h2>
        {this.state.todos.map(todo => (
          <div>
            <h3>{todo.title}</h3>
            <p>{todo.text}</p>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
