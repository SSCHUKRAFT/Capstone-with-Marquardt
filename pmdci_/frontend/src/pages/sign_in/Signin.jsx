import './signin.css'
import MarquardtLogo from '../../assets/Marquardt Logo.png'
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Button, TextField } from '@mui/material';
import Axios from 'axios'

function getDestination(employeeID, engineers, operators){
  for (let i = 0; i < engineers.length; i++){
    if (engineers[i] == employeeID){
      return("/engineer")
    }
  }
  for (let j = 0; j < operators.length; j++){
    if (operators[j] == employeeID){
      return("/data-entry")
    }
  }
  return("/invalid-id")
}

const Signin = () => {
  const [employeeID, setEmployeeID] = useState();

  const [operators, setOperators] = useState([]);
  const [engineers, setEngineers] = useState([]);

  useEffect(() => {
    const id = setInterval(() => {  
      Axios.get('http://localhost:3001/api/getEngineers').then((response)=> {
        setEngineers(response.data)
      
      })
      Axios.get('http://localhost:3001/api/getOperators').then((response)=> {
        setOperators(response.data)
      })
    }, 100)
    return () => clearInterval(id);
  }, [engineers, operators]);

  return(
    <div className="sign_in">
      <div className="sign_in_container">
        <img src={MarquardtLogo} alt="Logo"/>
        <h1>Welcome to Marquardt!</h1>
        <p>Please enter your ID below:</p>
        <TextField 
          type="number"
          hiddenLabel
          placeholder="ID"
          id="passed-parts-text"
          autoComplete="off"
          inputProps={{ inputMode: 'numeric', pattern: '[0-1000]*', style: {fontSize: 40} }}
          InputLabelProps={{ style: {fontSize: 40} }}
          sx={{ maxWidth: 300 }}
          onChange={(e) => setEmployeeID(e.target.value)}
        />
        <Link className="sign_in_link" to={getDestination(employeeID, engineers, operators)} >
          <Button 
          variant="contained" 
          color="success"
          style={{ fontSize: '32px', height: '60px', width: '200px' }}
          >
            Sign In
          </Button>
        </Link>
      </div>
    </div>
  );
};

export default Signin