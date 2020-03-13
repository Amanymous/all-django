import React from 'react';
import './App.css';
import Header from './components/header';
import Footer from './components/footer';

// import {Header} from './components/header';

function createAlert(){
  alert('hi there click here');
}

function ShowMessage(props){
  return <h2>My Message</h2>
}

function App() {
  return (
    <div className="App">
       <Header info='this is my message' mynum='9'/>
       <Header info='this is my message1' mynum='99'/>

        <a>
          react and django
        </a> 
        <Footer trademark="page by aman" 
       on myalert={createAlert}/>
       <ShowMessage toShow={true}/>
    </div>
  );
}

export default App;
// --------------------------------------------------






// import React from 'react';
// import './App.css';
// import Header from './components/header';
// import Footer from './components/footer';

// // import {Header} from './components/header';

// function App() {
//   return (
//     <div className="App">
//        <Header info='this is my message' mynum='9'/>
//        <Header info='this is my message1' mynum='99'/>

//         <a>
//           react and django
//         </a> 
//         <Footer trademark="page by aman"/>
//     </div>
//   );
// }

// export default App;

