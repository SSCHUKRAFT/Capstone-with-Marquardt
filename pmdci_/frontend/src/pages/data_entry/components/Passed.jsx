import React, { useState } from "react";
import { Button, TextField } from '@mui/material';
import './passed.css';
import Axios from 'axios'

const Passed = ({machine}, {language}) => {
  
  const [passedCount, setPassedCount] = useState("")

  const submitPassed = () => {
      Axios.post("http://localhost:3001/api/insert/passed", {
        passedCount: passedCount, 
        machine: machine,
      }).then(()=> {
        alert("successful insert")
      })
    };

  return (
    <div className="passed">
      <p>Passed Parts</p>
      <div className="passed_entry">
        <TextField 
          type="number"
          hiddenLabel
          placeholder="Parts"
          id="passed-parts-text"
          autoComplete="off"
          inputProps={{ inputMode: 'numeric', pattern: '[0-1000]*', style: {fontSize: 40} }}
          InputLabelProps={{ style: {fontSize: 40} }}
          sx={{ maxWidth: 200 }}
          onChange={(e) => setPassedCount(e.target.value)}
        >
        </TextField>
        <Button 
        variant="contained" 
        color="success"
        style={{ fontSize: '32px', height: '60px', width: '200px' }}
        onClick={submitPassed}
        >
          Enter
        </Button>
      </div>
    </div>
  );
};

export default Passed;