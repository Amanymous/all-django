import React from 'react';

function MovieList(props){
//    const movies=["harry potter","mission impossible"]
    return (
        <React.Fragment>
            {props.movies.map(movie=>{
                return <h3>{movie}</h3>
            })}
        </React.Fragment>
    )
}
export default MovieList;
// -----------------------------------------------

// import React from 'react';

// function MovieList(){
//     const movies=['edgae of tomorrow','incidious'];
//     return (
//         <h3>List of movies</h3>
      
     
//     )
// }
// export default MovieList;


