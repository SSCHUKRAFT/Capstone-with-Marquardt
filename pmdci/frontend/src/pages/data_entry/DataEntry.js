import React, { useState } from "react";
import './dataEntry.css'
import { Passed, Failed, Downtime, Graph } from './components';
import IconButton from '@mui/material/IconButton';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import LogoutIcon from '@mui/icons-material/Logout';
import Box from '@mui/material/Box';
import MenuItem from '@mui/material/MenuItem';
import { TextField } from "@mui/material";
import { Link } from "react-router-dom";

function DataEntry() {
  // const [passedCount, setPassedCount] = useState("")
  // const [failedCount, setFailedCount] = useState("")
  // const [retestedCount, setRetestedCount] = useState("")
  // const [downtime, setDowntime] = useState("")
  // const [cycletime, setCycletime] = useState("")
  // const [errorCode, setErrorCode] = useState("")
  // const [downtimeDesc, setDowntimeDesc] = useState("")
  const [machine, setMachine] = React.useState("");
  const [language, setLanguage] = React.useState("");
  const handleMachineChange = e => setMachine(e.target.value);
  const handleLanguageChange = e => setLanguage(e.target.value);

  return (
    <div className="App">
      <div className="sidebar">
        <IconButton aria-label="switch_user" size="large">
            <AccountCircleIcon style={{ color: 'black', fontSize: '3rem' }} />
          </IconButton>
        <Link to={"/"}>
          <IconButton aria-label="logout" size="large">
            <LogoutIcon style={{ color: 'black', fontSize: '3rem' }} />
          </IconButton>
        </Link>
      </div>
      <div className="content">
      <div className="header">
        <div className="part_family">
          <p>Welcome John, you are currently working with part family:</p>
          <Box className="machine_select">
            <TextField
              labelId="machine-select-label"
              id="machine-select"
              select
              label="Part Family"
              onChange={handleMachineChange}
              sx={{ minWidth: 200 }}
              size="small"
              color="info"
            >
              <MenuItem key={1} value={"Ford"}>Ford</MenuItem>
              <MenuItem key={2} value={"Cadillac"}>Cadillac</MenuItem>
              <MenuItem key={3} value={"Toyota"}>Toyota</MenuItem>
            </TextField>
          </Box>
        </div>
      <div className="language">
        <Box className="language_select">
          <TextField
            labelId="language-select-label"
            id="language-select"
            select
            variant="filled"
            label="Language"
            onChange={handleLanguageChange}
            sx={{ minWidth: 150 }}
            size="small"
            color="info"
          >
            <MenuItem value={"English"}>English</MenuItem>
            <MenuItem value={"Español"}>Español</MenuItem>
            <MenuItem value={"Deutsch"}>Deutsch</MenuItem>
          </TextField>
        </Box>
      </div>
    </div>
        <div className="container">
          <Passed machine={machine}/>
          <div className="divider" />
          <Failed machine={machine}/>
          <Graph machine={machine}/>
          <Downtime machine={machine}/>
        </div>
      </div>
    </div>
  );
}

export default DataEntry;
