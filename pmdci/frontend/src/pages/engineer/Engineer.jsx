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
  const [value, setValue] = React.useState(0)

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
        <Box sx={{ width: '80%', height: '100%'}}>
          <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
            <Tabs value={value} onChange={handleChange} aria-label="basic tabs example" centered>
              <Tab label="First Shift" {...a11yProps(0)} />
              <Tab label="Second Shift" {...a11yProps(1)} />
              <Tab label="Third Shift" {...a11yProps(2)} />
            </Tabs>
          </Box>
          <TabPanel value={value} index={0}>
            <div className="table">
              <table>
                <tr className="table_header">
                  <th>Hour</th>
                  <th>6</th>
                  <th>7</th>
                  <th>8</th>
                  <th>9</th>
                  <th>10</th>
                  <th>11</th>
                  <th>12</th>
                  <th>13</th>
                  <th>14</th>
                  <th>15</th>
                </tr>
                <tr className="expected_row">
                  <th>Expected Passed</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                </tr>
                <tr>
                  <th>Expected Failed</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                </tr>
                <tr>
                  <th>UCL</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                </tr>
              </table>
            </div>
          </TabPanel>
          <TabPanel value={value} index={1}>
          <div className="table">
              <table>
                <tr className="table_header">
                  <th>Hour</th>
                  <th>16</th>
                  <th>17</th>
                  <th>18</th>
                  <th>19</th>
                  <th>20</th>
                  <th>21</th>
                  <th>22</th>
                  <th>23</th>
                  <th>1</th>
                  <th>2</th>
                </tr>
                <tr className="expected_row">
                  <th>Expected Passed</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                </tr>
                <tr>
                  <th>Expected Failed</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                </tr>
                <tr>
                  <th>UCL</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                </tr>
              </table>
            </div>
          </TabPanel>
          <TabPanel value={value} index={2}>
          <div className="table">
              <table>
                <tr className="table_header">
                  <th>Hour</th>
                  <th>6</th>
                  <th>7</th>
                  <th>8</th>
                  <th>9</th>
                  <th>10</th>
                  <th>11</th>
                  <th>12</th>
                  <th>13</th>
                  <th>14</th>
                  <th>15</th>
                  <th>16</th>
                  <th>17</th>
                </tr>
                <tr className="expected_row">
                  <th>Expected Passed</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                  <th>230</th>
                </tr>
                <tr>
                  <th>Expected Failed</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                  <th>4</th>
                </tr>
                <tr>
                  <th>UCL</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                  <th>8</th>
                </tr>
              </table>
            </div>
          </TabPanel>
        </Box>
      </div>
    </div>
  );
};
  
export default Engineer