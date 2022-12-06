import './edit.css'
import React, { useState } from "react";
import { Button, TextField } from '@mui/material';
import Axios from 'axios'

const Edit = (props) => {
  const [passedCount, setPassedCount] = useState()

  const submitPassed = () => {
      Axios.post("http://localhost:3001/api/edit/passed/" + props.hour, {
        passedCount: passedCount, 
        machine: props.machine,
      }).then(()=> {
        alert("successful insert")
      })
    };

  return(props.trigger) ? (
      <div className="edit">
          <div className="edit_title">You are editing the {props.field} entered at {props.hour}:00.</div>
          <button className="close_button" onClick={() => props.setTrigger(false)}>X</button>
          <TextField 
          type="number"
          hiddenLabel
          placeholder="Parts"
          id="passed-parts-text"
          autoComplete="off"
          inputProps={{ inputMode: 'numeric', pattern: '[0-1000]*', style: {fontSize: 24} }}
          InputLabelProps={{ style: {fontSize: 24} }}
          sx={{ maxWidth: 200 }}
          stlye={{ height: '60px' }}
          onChange={(e) => setPassedCount(e.target.value)}
          >
          </TextField>
          <Button 
          variant="contained" 
          color="success"
          style={{ fontSize: '32px', height: '60px', width: '200px' }}
          onClick={() => {
            submitPassed();
            props.setTrigger(false);
          }}
          >
          Enter
          </Button>
      </div>
  ) : "";
}

export default Edit