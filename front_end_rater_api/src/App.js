import React,{ Component } from 'react';
import MovieList from './components/movie-list';
import './App.css';

class App extends Component {
 movies=['edgae of tomorrow','incidious'];
 componentDidMount(){
   fetch('http://127.0.0.1:8000/api/movies/',{
     method:"GET",
     headers:{
       'Authorization':''
     }
   }).then(resp=>console.log(resp))
   .catch(error=>console.log(error))
   
 }

render(){
  return (
    <div className="App">
       <h1>Movie Rater Api</h1>
       <MovieList movies={this.movies}/>
    </div>
  );
}}

export default App;
