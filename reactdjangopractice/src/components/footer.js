import React,  { Component } from 'react';

class Footer extends Component{

    state={
       name: '',
       age:19
    }

    componentDidMount(){
        this.setState({name: 'MyName'});
        
    }
   

    changed = evt =>{
        console.log('aman mirza',evt.target.value);
        console.log(this.state.name)

        // this.state.name=evt.target.value;
        // this.setState({name:evt.target.value})

    }
    
    render(){
    return(<div>
        {this.state.age===19 ? (
            <React.Fragment>
     <h2 onClick={this.props.myalert}>
        this is Footer {this.props.trademark}</h2>
        <input value ={this.props.name}
        onChange={this.changed} type="text"/>
        </React.Fragment>
         ):"no"}

        </div>
     )}}
export default Footer;

// --------------------------------------------------------
// import React,  { Component } from 'react';

// class Footer extends Component{
//     render(){
//     return <h2>this is Footer {this.props.trademark}</h2>
//     }

// }
// export default Footer;