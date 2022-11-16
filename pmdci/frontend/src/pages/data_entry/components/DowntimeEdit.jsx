import './downtimeEdit.css'
import React, { useState } from "react";
import { Button, TextField } from '@mui/material';
import Axios from 'axios'

const DowntimeEdit = (props) => {
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
      <div className="downtime_edit">
        <button className="downtime_close_button" onClick={() => props.setTrigger(false)}>X</button>
        <div className="downtime_table">
          <table>
            <tr className="downtime_table_header">
              <th>ID</th>
              <th>Downtime</th>
              <th>Error Code</th>
              <th>Escalation Time</th>
              <th>Description</th>
            </tr>
          </table>
        </div>
      </div>
  ) : "";
}

export default DowntimeEdit