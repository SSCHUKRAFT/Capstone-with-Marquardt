import './downtime.css';
import { Button, TextField } from '@mui/material';
import React, { useState } from "react";
import MenuItem from '@mui/material/MenuItem';
import Axios from 'axios'


const Downtime = ({machine}, {language}) => {
  const [downtime, setDowntime] = useState("")
  const [esclTime, setEsclTime] = useState("")
  const [errorCode, setErrorCode] = React.useState("");
  const [description, setDescription] = React.useState("");

  const submitDowntime = () => {
    Axios.post("http://localhost:3001/api/insert/downtime", {
      downtime: downtime,
      esclTime: esclTime,
      errorCode: errorCode,
      description: description,
      machine: machine,
    }).then(()=> {
      alert("successful insert")
    })
  };

  return (
    <div className="downtime">
      <div className="downtime_data">
        <div className="downtime_duration">
          <text>Downtime</text>
          <TextField 
          hiddenLabel
          placeholder="Minutes"
          type="number"
          autoComplete="off"
          id="downtime-duration-text"
          inputProps={{ inputMode: 'numeric', pattern: '[0-100]*', style: {fontSize: 20} }}
          InputLabelProps={{ style: {fontSize: 20} }}
          sx={{ maxWidth: 200 }}
          onChange={(e) => setDowntime(e.target.value)}
        >
        </TextField>
        </div>
        <div className="escltime">
          <text>Escalation Time</text>
          <TextField 
          hiddenLabel
          type="number"
          autoComplete="off"
          placeholder="Minutes"
          id="escalationtime-duration-text"
          inputProps={{ inputMode: 'numeric', pattern: '[0-100]*', style: {fontSize: 20} }}
          InputLabelProps={{ style: {fontSize: 20} }}
          sx={{ maxWidth: 200 }}
          onChange={(e) => setEsclTime(e.target.value)}
        >
        </TextField>
        </div>
        <div className="error_code">
          <text>Error Code</text>
          <TextField
                labelId="errorCode-select-label"
                id="errorCode-select"
                select
                autoComplete="off"
                variant="filled"
                value={errorCode}
                label="Error Code"
                onChange={(e) => setErrorCode(e.target.value)}
                sx={{ minWidth: 200 }}
                InputLabelProps={{ style: {fontSize: 20} }}
                size="small"
                color="info"
              >
                <MenuItem value={"100 - Machine Fire"} sx={{ fontSize: 20 }}>101 - Machine Fire</MenuItem>
                <MenuItem value={"101 - Tripped"} sx={{ fontSize: 20 }}>102 - Tripped</MenuItem>
                <MenuItem value={"102 - Fell Asleep"} sx={{ fontSize: 20 }}>103 - Fell Asleep</MenuItem>
              </TextField>
        </div>
        <div className="error_desc">
          <text>Error Description</text>
          <TextField 
          hiddenLabel
          autoComplete="off"
          placeholder="Description"
          id="downtime-description-text"
          inputProps={{ inputMode: 'numeric', pattern: '[0-100]*', style: {fontSize: 24} }}
          InputLabelProps={{ style: {fontSize: 24} }}
          sx={{ maxWidth: 400 }}
          onChange={(e) => setDescription(e.target.value)}
        >
        </TextField>
        </div>
      </div>
      <div className="downtime_enter_btn">
        <Button 
          variant="contained" 
          color="success"
          style={{ fontSize: '32px', height: '60px', width: '200px' }}
          onClick={submitDowntime}
          >
            Enter
        </Button>
      </div>
    </div>
  );
};

export default Downtime;