import './edit.css'
import React, { useState } from "react";
import { Button, TextField } from '@mui/material';

const Edit = (props) => {
    const [passedCount, setPassedCount] = useState()
    
    return(props.trigger) ? (
        <div className="edit">
            <div className="edit_title">You are editing parts entered at {props.hour}:00.</div>
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
            // onClick={}
            >
            Enter
            </Button>
        </div>
    ) : "";
}

export default Edit