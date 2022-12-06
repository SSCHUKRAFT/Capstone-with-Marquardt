import React from "react";
import './engineer.css'
import PropTypes from 'prop-types';
import Tab from '@mui/material/Tab';
import Tabs from '@mui/material/Tabs';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import IconButton from '@mui/material/IconButton';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import LogoutIcon from '@mui/icons-material/Logout';
import { Link } from "react-router-dom";
import Edit from './Edit'

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.number.isRequired,
  value: PropTypes.number.isRequired,
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

const Engineer = () => {
  const [value, setValue] = React.useState(0);
  const [popup, setPopup] = React.useState(false);
  const [popupHour, setPopupHour] = React.useState();
  const [field, setField] = React.useState();

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };
  
  return(
    <div className="engineer">
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
      <div className="engineer_container">
        <div className="engineer_tab_table">
          <Box sx={{ width: '80%', height: '100%'}}>
            <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
              <Tabs value={value} onChange={handleChange} aria-label="basic tabs example" centered>
                <Tab label="First Shift" {...a11yProps(0)} />
                <Tab label="Second Shift" {...a11yProps(1)} />
                <Tab label="Third Shift" {...a11yProps(2)} />
              </Tabs>
              <Edit hour={popupHour} trigger={popup} setTrigger={setPopup} field={field}></Edit>
            </Box>
            <TabPanel value={value} index={0}>
              <div className="table_wrapper">
                <table class="styled_table">
                  <thead>
                    <tr>
                      <th>Hour</th>
                      <th>Expected Passed</th>
                      <th>Expected Failed</th>
                      <th>UCL</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>6</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(6); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(6); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(6); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>7</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(7); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(7); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(7); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>8</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(8); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(8); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(8); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>9</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(9); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(9); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(9); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>10</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(10); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(10); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(10); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>11</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(11); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(11); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(11); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>12</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(12); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(12); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(12); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>13</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(13); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(13); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(13); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>14</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(14); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(14); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(14); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>15</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(15); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(15); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(15); setField("UCL")}}>8</button></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </TabPanel>
            <TabPanel value={value} index={1}>
            <div className="table_wrapper">
              <table class="styled_table">
                  <thead>
                    <tr>
                      <th>Hour</th>
                      <th>Expected Passed</th>
                      <th>Expected Failed</th>
                      <th>UCL</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>16</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(16); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(16); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(16); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>17</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(17); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(17); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(17); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>18</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(18); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(18); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(18); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>19</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(19); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(19); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(19); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>20</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(20); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(20); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(20); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>21</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(21); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(21); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(21); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>22</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(22); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(22); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(22); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>23</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(23); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(23); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(23); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>1</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(1); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(1); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(1); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(2); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(2); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(2); setField("UCL")}}>8</button></td>
                    </tr>
                  </tbody>
              </table>
            </div>
            </TabPanel>
            <TabPanel value={value} index={2}>
            <div className="table_wrapper">
              <table class="styled_table">
                  <thead>
                    <tr>
                      <th>Hour</th>
                      <th>Expected Passed</th>
                      <th>Expected Failed</th>
                      <th>UCL</th>
                    </tr>
                  </thead>
                  <tbody>
                  <tr>
                      <td>6</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(6); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(6); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(6); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>7</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(7); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(7); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(7); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>8</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(8); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(8); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(8); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>9</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(9); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(9); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(9); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>10</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(10); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(10); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(10); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>11</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(11); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(11); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(11); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>12</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(12); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(12); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(12); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>13</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(13); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(13); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(13); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>14</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(14); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(14); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(14); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>15</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(15); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(15); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(15); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>16</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(16); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(16); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(16); setField("UCL")}}>8</button></td>
                    </tr>
                    <tr>
                      <td>17</td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(17); setField("expected passed parts")}}>230</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(17); setField("expected failed parts")}}>4</button></td>
                      <td><button className="popup_button" onClick={() => {setPopup(true); setPopupHour(17); setField("UCL")}}>8</button></td>
                    </tr>
                  </tbody>
              </table>
            </div>
            </TabPanel>
          </Box>
        </div>
      </div>
    </div>
  );
};
  
export default Engineer