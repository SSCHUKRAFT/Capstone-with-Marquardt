import './header.css';
import Box from '@mui/material/Box';
import MenuItem from '@mui/material/MenuItem';
import { TextField } from "@mui/material";
import { useRef } from 'react';

const Header = ({setMachine}, {setLanguage}) => {
  
  const machineRef = useRef('')
  const languageRef = useRef('')
  
  const onMachineSelect = () => {
    setMachine(machineRef.current.valueOf)
  }

  const onLanguageSelect = () => {
    setLanguage(languageRef.current.valueOf)
  }

  return (
    <div className="header">
      <div className="machine">
        <p>Welcome John, you are currently operating machine:</p>
        <Box className="machine_select">
          <TextField
            inputRef={machineRef}
            labelId="machine-select-label"
            id="machine-select"
            select
            label="Machine"
            onChange={onMachineSelect}
            sx={{ minWidth: 200 }}
            size="small"
            color="info"
          >
            <MenuItem key={1} value={"Machine One"}>Machine One</MenuItem>
            <MenuItem key={2} value={"Machine Two"}>Machine Two</MenuItem>
            <MenuItem key={3} value={"Machine Three"}>Machine Three</MenuItem>
          </TextField>
        </Box>
      </div>
      <div className="language">
        <Box className="language_select">
          <TextField
            inputRef={languageRef}
            labelId="language-select-label"
            id="language-select"
            select
            variant="filled"
            label="Language"
            onChange={onLanguageSelect}
            sx={{ minWidth: 150 }}
            size="small"
            color="info"
          >
            <MenuItem key={1} value={"English"}>English</MenuItem>
            <MenuItem key={2} value={"Español"}>Español</MenuItem>
            <MenuItem key={3} value={"Deutsch"}>Deutsch</MenuItem>
          </TextField>
        </Box>
      </div>
    </div>
  );
};

export default Header;