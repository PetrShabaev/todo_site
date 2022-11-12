import './App.css';
import React from 'react'
import UserList from './components/users';
import axios from 'axios';
import Header from './components/header';
import Footer from './components/footer';


class App extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      'users':[]
    }
  }

   componentDidMount(){
   axios.get('http://127.0.0.1:8000/api/users/')
     .then(response => {
       const users = response.data
         this.setState(
         {
           'users': users
         }
       )
       }).catch(error => console.log(error))
     }

   render () {
     return (
       <div className='wrapper'>
          
           <Header />
          
           <UserList users={this.state.users} />
          
           <Footer />
          
       </div>
     )
   }
}

export default App;
