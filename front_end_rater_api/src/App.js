import React,{ Component } from 'react';
import MovieList from './components/movie-list';
import './App.css';

class App extends Component {
 movies=['edgae of tomorrow','incidious'];

render(){
  return (
    <div className="App">
       <h1>Movie Rater Api</h1>
       <MovieList movies={this.movies}/>
    </div>
  );
}}

export default App;
