import React, { useState } from "react";
import { Button, TextField } from '@mui/material';
import './failed.css';
import Axios from 'axios'

const Failed = ({machine}, {language}) => {

  const [failedCount, setFailedCount] = useState("")
  const [retestedCount, setRetestedCount] = useState("")

  const submitFailed = () => {
    Axios.post("http://localhost:3001/api/insert/failed", {
      failedCount: failedCount, 
      machine: machine,
    }).then(()=> {
      alert("successful insert")
    })
  };

  const submitRetested = () => {
      Axios.post("http://localhost:3001/api/insert/retested", {
        retestedCount: retestedCount, 
        machine: machine,
      }).then(()=> {
        alert("successful insert")
      })
    };

  return (
    <div className="failed">
      <p>Failed Parts</p>
      <div className="failed_entry">
        <TextField 
          hiddenLabel
          type="number"
          placeholder="Parts"
          autoComplete="off"
          id="failed-parts-text"
          inputProps={{ inputMode: 'numeric', pattern: '[0-100]*', style: {fontSize: 24} }}
          InputLabelProps={{ style: {fontSize: 24} }}
          sx={{ maxWidth: 200 }}
          onChange={(e) => setFailedCount(e.target.value)}
        >
        </TextField>
        <Button 
        variant="contained" 
        color="success"
        style={{ fontSize: '32px', height: '60px', width: '200px' }}
        onClick={submitFailed}
        >
          Enter
        </Button>
      </div>
      <div className="retry_entry">
        <TextField 
          hiddenLabel
          placeholder="Parts"
          type="number"
          autoComplete="off"
          id="failed-parts-text"
          inputProps={{ inputMode: 'numeric', pattern: '[0-100]*', style: {fontSize: 24} }}
          InputLabelProps={{ style: {fontSize: 24} }}
          sx={{ maxWidth: 200 }}
          onChange={(e) => setRetestedCount(e.target.value)}
        >
        </TextField>
        <Button 
        variant="contained" 
        color="warning"
        style={{ fontSize: '32px', height: '60px', width: '200px' }}
        onClick={submitRetested}
        >
          Retry
        </Button>
      </div>
    </div>
  );
};

export default Failed;