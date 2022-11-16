import './graph.css';
import React, { useState, useEffect } from "react";
import Axios from 'axios'
import { Bar } from "react-chartjs-2";
import { Chart, CategoryScale, LinearScale, BarElement } from "chart.js";
import ChartDataLabels from 'chartjs-plugin-datalabels';
import Edit from './Edit.jsx';

Chart.register(CategoryScale, LinearScale, BarElement, ChartDataLabels)
Chart.defaults.set('plugins.datalabels', {
  color: '#000000'
});

function getPassedChartColors(expectedPassed, passedSumSix, passedSumSeven, passedSumEight, passedSumNine, passedSumTen, passedSumEleven, passedSumTwelve, passedSumThirteen, passedSumFourteen, passedSumFifteen){
  const green = "rgb(62, 160, 85)"
  const yellow = "rgb(255, 216, 1)"
  const red = "rgb(244, 76, 76)"
  const colors = [
    green,
    green,
    green,
    green,
    green,
    green,
    green,
    green,
    green,
    green
  ]

  if (passedSumSix < 180){
    colors[0] = red
  }else if (passedSumSix < expectedPassed){
    colors[0] = yellow
  }

  if (passedSumSeven < 180){
    colors[1] = red
  }else if (passedSumSeven < expectedPassed){
    colors[1] = yellow
  }

  if (passedSumEight < 180){
    colors[2] = red
  }else if (passedSumEight < expectedPassed){
    colors[2] = yellow
  }

  if (passedSumNine < 180){
    colors[3] = red
  }else if (passedSumNine < expectedPassed){
    colors[3] = yellow
  }

  if (passedSumTen < 180){
    colors[4] = red
  }else if (passedSumTen < expectedPassed){
    colors[4] = yellow
  }

  if (passedSumEleven < 180){
    colors[5] = red
  }else if (passedSumEleven < expectedPassed){
    colors[5] = yellow
  }

  if (passedSumTwelve < 180){
    colors[6] = red
  }else if (passedSumTwelve < expectedPassed){
    colors[6] = yellow
  }

  if (passedSumThirteen < 180){
    colors[7] = red
  }else if (passedSumThirteen < expectedPassed){
    colors[7] = yellow
  }

  if (passedSumFourteen < 180){
    colors[8] = red
  }else if (passedSumFourteen < expectedPassed){
    colors[8] = yellow
  }

  if (passedSumFifteen < 180){
    colors[9] = red
  }else if (passedSumFifteen < expectedPassed){
    colors[9] = yellow
  }

  return colors
}

function getFailedChartColors(expectedFailed, failedSumSix, failedSumSeven, failedSumEight, failedSumNine, failedSumTen, failedSumEleven, failedSumTwelve, failedSumThirteen, failedSumFourteen, failedSumFifteen){
  const green = "rgb(62, 160, 85)"
  const yellow = "rgb(255, 216, 1)"
  const red = "rgb(244, 76, 76)"
  const colors = [
    green,
    green,
    green,
    green,
    green,
    green,
    green,
    green,
    green,
    green
  ]

  if (failedSumSix > 6){
    colors[0] = red
  }else if (failedSumSix > expectedFailed){
    colors[0] = yellow
  }

  if (failedSumSeven > 6){
    colors[1] = red
  }else if (failedSumSeven > expectedFailed){
    colors[1] = yellow
  }

  if (failedSumEight > 6){
    colors[2] = red
  }else if (failedSumEight > expectedFailed){
    colors[2] = yellow
  }

  if (failedSumNine > 6){
    colors[3] = red
  }else if (failedSumNine > expectedFailed){
    colors[3] = yellow
  }

  if (failedSumTen > 6){
    colors[4] = red
  }else if (failedSumTen > expectedFailed){
    colors[4] = yellow
  }

  if (failedSumEleven > 6){
    colors[5] = red
  }else if (failedSumEleven > expectedFailed){
    colors[5] = yellow
  }

  if (failedSumTwelve > 6){
    colors[6] = red
  }else if (failedSumTwelve > expectedFailed){
    colors[6] = yellow
  }

  if (failedSumThirteen > 6){
    colors[7] = red
  }else if (failedSumThirteen > expectedFailed){
    colors[7] = yellow
  }

  if (failedSumFourteen > 6){
    colors[8] = red
  }else if (failedSumFourteen > expectedFailed){
    colors[8] = yellow
  }

  if (failedSumFifteen > 6){
    colors[9] = red
  }else if (failedSumFifteen > expectedFailed){
    colors[9] = yellow
  }

  return colors
}

function currentTime(date, prop){
  if (date.getHours() === prop){
    return 'rgba(0, 209, 251)'
  }else{
    return 'transparent'
  }
}

const Graph = ({machine}) => {
  const [date, setDate] = useState(new Date())
  const styleSix = {
    backgroundColor: currentTime(date, 6),
  };
  const styleSeven = {
    backgroundColor: currentTime(date, 7),
  };
  const styleEight = {
    backgroundColor: currentTime(date, 8),
  };
  const styleNine = {
    backgroundColor: currentTime(date, 9),
  };
  const styleTen = {
    backgroundColor: currentTime(date, 10),
  };
  const styleEleven = {
    backgroundColor: currentTime(date, 11),
  };
  const styleTwelve = {
    backgroundColor: currentTime(date, 12),
  };
  const styleThirteen = {
    backgroundColor: currentTime(date, 13),
  };
  const styleFourteen = {
    backgroundColor: currentTime(date, 14),
  };
  const styleFifteen = {
    backgroundColor: currentTime(date, 15),
  };
  
  const [popup, setPopup] = useState(false);
  const [popupHour, setPopupHour] = useState();
  const [popupParts, setPopupParts] = useState();
  
  const expectedPassed = 230
  const expectedFailed = 4

  const [passedSumSix, setPassedSumSix] = useState("0")
  const [passedSumSeven, setPassedSumSeven] = useState("0")
  const [passedSumEight, setPassedSumEight] = useState("0")
  const [passedSumNine, setPassedSumNine] = useState("0")
  const [passedSumTen, setPassedSumTen] = useState("0")
  const [passedSumEleven, setPassedSumEleven] = useState("0")
  const [passedSumTwelve, setPassedSumTwelve] = useState("0")
  const [passedSumThirteen, setPassedSumThirteen] = useState("0")
  const [passedSumFourteen, setPassedSumFourteen] = useState("0")
  const [passedSumFifteen, setPassedSumFifteen] = useState("0")

  const [totalPassedSumSeven, setTotalPassedSumSeven] = useState("0")
  const [totalPassedSumEight, setTotalPassedSumEight] = useState("0")
  const [totalPassedSumNine, setTotalPassedSumNine] = useState("0")
  const [totalPassedSumTen, setTotalPassedSumTen] = useState("0")
  const [totalPassedSumEleven, setTotalPassedSumEleven] = useState("0")
  const [totalPassedSumTwelve, setTotalPassedSumTwelve] = useState("0")
  const [totalPassedSumThirteen, setTotalPassedSumThirteen] = useState("0")
  const [totalPassedSumFourteen, setTotalPassedSumFourteen] = useState("0")
  const [totalPassedSumFifteen, setTotalPassedSumFifteen] = useState("0")

  const [failedSumSix, setFailedSumSix] = useState("0")
  const [failedSumSeven, setFailedSumSeven] = useState("0")
  const [failedSumEight, setFailedSumEight] = useState("0")
  const [failedSumNine, setFailedSumNine] = useState("0")
  const [failedSumTen, setFailedSumTen] = useState("0")
  const [failedSumEleven, setFailedSumEleven] = useState("0")
  const [failedSumTwelve, setFailedSumTwelve] = useState("0")
  const [failedSumThirteen, setFailedSumThirteen] = useState("0")
  const [failedSumFourteen, setFailedSumFourteen] = useState("0")
  const [failedSumFifteen, setFailedSumFifteen] = useState("0")

  const [totalFailedSumSeven, setTotalFailedSumSeven] = useState("0")
  const [totalFailedSumEight, setTotalFailedSumEight] = useState("0")
  const [totalFailedSumNine, setTotalFailedSumNine] = useState("0")
  const [totalFailedSumTen, setTotalFailedSumTen] = useState("0")
  const [totalFailedSumEleven, setTotalFailedSumEleven] = useState("0")
  const [totalFailedSumTwelve, setTotalFailedSumTwelve] = useState("0")
  const [totalFailedSumThirteen, setTotalFailedSumThirteen] = useState("0")
  const [totalFailedSumFourteen, setTotalFailedSumFourteen] = useState("0")
  const [totalFailedSumFifteen, setTotalFailedSumFifteen] = useState("0")

  const passedData = {
    labels: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    datasets: [
      {
        label: "First set",
        data: [passedSumSix, passedSumSeven, passedSumEight, passedSumNine, passedSumTen, passedSumEleven, passedSumTwelve, passedSumThirteen, passedSumFourteen, passedSumFifteen],
        backgroundColor: getPassedChartColors(expectedPassed, passedSumSix, passedSumSeven, passedSumEight, passedSumNine, passedSumTen, passedSumEleven, passedSumThirteen, passedSumFourteen, passedSumFifteen),
        borderColor: "black",
        borderWidth: 1
      }
    ]
  };

  const passedOptions = {
    legend: {
      display: false
    },
    responsive: false,
    scales: {
      xAxes: 
        {
          grid: {
            display: false,
            drawBorder: false,
            borderDash: [3, 3],
            zeroLineColor: "transparent",
          },
          categoryPercentage: 1,
          barPercentage: 0.9,
          ticks: {
            beginAtZero: false,
            display: false
          }
        }
      ,
      yAxes: 
        {
          display: false,
          gridLines: {
            display: false,
            zeroLineColor: "transparent"
          },
          ticks: {
            min: 0,
            max: 460,
            beginAtZero: true,
            display: false
          }
        }
      
    }
  };

  const failedData = {
    labels: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    datasets: [
      {
        label: "First set",
        data: [failedSumSix, failedSumSeven, failedSumEight, failedSumNine, failedSumTen, failedSumEleven, failedSumTwelve, failedSumThirteen, failedSumFourteen, failedSumFifteen],
        backgroundColor: getFailedChartColors(expectedFailed, failedSumSix, failedSumSeven, failedSumEight, failedSumNine, failedSumTen, failedSumEleven, failedSumTwelve, failedSumThirteen, failedSumFourteen, failedSumFifteen),
        borderColor: "black",
        borderWidth: 1
      }
    ]
  };

  const failedOptions = {
    legend: {
      display: false
    },
    responsive: false,
    scales: {
      xAxes: 
        {
          grid: {
            display: false,
            drawBorder: false,
            borderDash: [3, 3],
            zeroLineColor: "transparent",
          },
          categoryPercentage: 1,
          barPercentage: 0.9,
          ticks: {
            beginAtZero: false,
            display: false
          }
        }
      ,
      yAxes: 
        {
          display: false,
          gridLines: {
            display: false,
            zeroLineColor: "transparent"
          },
          ticks: {
            min: 0,
            max: 460,
            beginAtZero: true,
            display: false
          }
        }
      
    }
  };

  useEffect(() => {
    const id = setInterval(() => {  
      setDate(new Date())
      Axios.get('http://localhost:3001/api/getPassedSum/six').then((response)=> {
        setPassedSumSix(response.data)
      })
      Axios.get('http://localhost:3001/api/getPassedSum/seven').then((response)=> {
        setPassedSumSeven(response.data)
        setTotalPassedSumSeven(passedSumSix + passedSumSeven)
      })
      Axios.get('http://localhost:3001/api/getPassedSum/eight').then((response)=> {
        setPassedSumEight(response.data)
        setTotalPassedSumEight(totalPassedSumSeven + passedSumEight)
      })
      Axios.get('http://localhost:3001/api/getPassedSum/nine').then((response)=> {
        setPassedSumNine(response.data)
        setTotalPassedSumNine(totalPassedSumEight + passedSumNine)
      })
      Axios.get('http://localhost:3001/api/getPassedSum/ten').then((response)=> {
        setPassedSumTen(response.data)
        setTotalPassedSumTen(totalPassedSumNine + passedSumTen)
      })
      Axios.get('http://localhost:3001/api/getPassedSum/eleven').then((response)=> {
        setPassedSumEleven(response.data)
        setTotalPassedSumEleven(totalPassedSumTen + passedSumEleven)
      })
      Axios.get('http://localhost:3001/api/getPassedSum/twelve').then((response)=> {
        setPassedSumTwelve(response.data)
        setTotalPassedSumTwelve(totalPassedSumEleven + passedSumTwelve)
      })
      Axios.get('http://localhost:3001/api/getPassedSum/thirteen').then((response)=> {
        setPassedSumThirteen(response.data)
        setTotalPassedSumThirteen(totalPassedSumTwelve + passedSumThirteen)
      })
      Axios.get('http://localhost:3001/api/getPassedSum/fourteen').then((response)=> {
        setPassedSumFourteen(response.data)
        setTotalPassedSumFourteen(totalPassedSumThirteen + passedSumFourteen)
      })
      Axios.get('http://localhost:3001/api/getPassedSum/fifteen').then((response)=> {
        setPassedSumFifteen(response.data)
        setTotalPassedSumFifteen(totalPassedSumFourteen + passedSumFifteen)
      })

      Axios.get('http://localhost:3001/api/getFailedSum/six').then((response)=> {
        setFailedSumSix(response.data)
      })
      Axios.get('http://localhost:3001/api/getFailedSum/seven').then((response)=> {
        setFailedSumSeven(response.data)
        setTotalFailedSumSeven(failedSumSix + failedSumSeven)
      })
      Axios.get('http://localhost:3001/api/getFailedSum/eight').then((response)=> {
        setFailedSumEight(response.data)
        setTotalFailedSumEight(totalFailedSumSeven + failedSumEight)
      })
      Axios.get('http://localhost:3001/api/getFailedSum/nine').then((response)=> {
        setFailedSumNine(response.data)
        setTotalFailedSumNine(totalFailedSumEight + failedSumNine)
      })
      Axios.get('http://localhost:3001/api/getFailedSum/ten').then((response)=> {
        setFailedSumTen(response.data)
        setTotalFailedSumTen(totalFailedSumNine + failedSumTen)
      })
      Axios.get('http://localhost:3001/api/getFailedSum/eleven').then((response)=> {
        setFailedSumEleven(response.data)
        setTotalFailedSumEleven(totalFailedSumTen + failedSumEleven)
      })
      Axios.get('http://localhost:3001/api/getFailedSum/twelve').then((response)=> {
        setFailedSumTwelve(response.data)
        setTotalFailedSumTwelve(totalFailedSumEleven + failedSumTwelve)
      })
      Axios.get('http://localhost:3001/api/getFailedSum/thirteen').then((response)=> {
        setFailedSumThirteen(response.data)
        setTotalFailedSumThirteen(totalFailedSumTwelve + failedSumThirteen)
      })
      Axios.get('http://localhost:3001/api/getFailedSum/fourteen').then((response)=> {
        setFailedSumFourteen(response.data)
        setTotalFailedSumFourteen(totalFailedSumThirteen + failedSumFourteen)
      })
      Axios.get('http://localhost:3001/api/getFailedSum/fifteen').then((response)=> {
        setFailedSumFifteen(response.data)
        setTotalFailedSumFifteen(totalFailedSumFourteen + failedSumFifteen)
      })
    }, 100)
    return () => clearInterval(id);
  }, [machine, passedSumSix, passedSumSeven, passedSumEight, passedSumNine, passedSumTen, passedSumEleven, passedSumTwelve, passedSumThirteen, 
    passedSumFourteen, passedSumFifteen, totalPassedSumSeven, totalPassedSumEight, totalPassedSumNine, totalPassedSumTen, totalPassedSumEleven, 
    totalPassedSumTwelve, totalPassedSumThirteen, totalPassedSumFourteen, totalPassedSumFifteen, failedSumSix, failedSumSeven, failedSumEight, 
    failedSumNine, failedSumTen, failedSumEleven, failedSumTwelve, failedSumThirteen, failedSumFourteen, failedSumFifteen, totalFailedSumSeven, 
    totalFailedSumEight, totalFailedSumNine, totalFailedSumTen, totalFailedSumEleven, totalFailedSumTwelve, totalFailedSumThirteen, totalFailedSumFourteen, 
    totalFailedSumFifteen, date]);
  
  return (
    <div className="graph">
      <div className="graph_label">
        <text>&nbsp;&nbsp;&nbsp;Time</text>
        <text>&nbsp;&nbsp;&nbsp;Parts</text>
        <text>&nbsp;&nbsp;&nbsp;Sum</text>
      </div>
      <div className="graph_data">
        <div className="tables">
          <div className="passed_table">
            <table>
              <tr className="table_header">
                <th style={styleSix}>6</th>
                <th style={styleSeven}>7</th>
                <th style={styleEight}>8</th>
                <th style={styleNine}>9</th>
                <th style={styleTen}>10</th>
                <th style={styleEleven}>11</th>
                <th style={styleTwelve}>12</th>
                <th style={styleThirteen}>13</th>
                <th style={styleFourteen}>14</th>
                <th style={styleFifteen}>15</th>
              </tr>
              <tr className="parts_row">
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(6); setPopupParts(passedSumSix)}}>{passedSumSix}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(7); setPopupParts(passedSumSeven)}}>{passedSumSeven}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(8); setPopupParts(passedSumEight)}}>{passedSumEight}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(9); setPopupParts(passedSumNine)}}>{passedSumNine}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(10); setPopupParts(passedSumTen)}}>{passedSumTen}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(11); setPopupParts(passedSumEleven)}}>{passedSumEleven}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(12); setPopupParts(passedSumTwelve)}}>{passedSumTwelve}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(13); setPopupParts(passedSumThirteen)}}>{passedSumThirteen}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(14); setPopupParts(passedSumFourteen)}}>{passedSumFourteen}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(15); setPopupParts(passedSumFifteen)}}>{passedSumFifteen}</button>
                </th>
              </tr>
              <tr>
                <th>{passedSumSix}</th>
                <th>{totalPassedSumSeven}</th>
                <th>{totalPassedSumEight}</th>
                <th>{totalPassedSumNine}</th>
                <th>{totalPassedSumTen}</th>
                <th>{totalPassedSumEleven}</th>
                <th>{totalPassedSumTwelve}</th>
                <th>{totalPassedSumThirteen}</th>
                <th>{totalPassedSumFourteen}</th>
                <th>{totalPassedSumFifteen}</th>
              </tr>
            </table>
          </div>
          <div className="failed_table">
            <table>
              <tr className="table_header">
                <th style={styleSix}>6</th>
                <th style={styleSeven}>7</th>
                <th style={styleEight}>8</th>
                <th style={styleNine}>9</th>
                <th style={styleTen}>10</th>
                <th style={styleEleven}>11</th>
                <th style={styleTwelve}>12</th>
                <th style={styleThirteen}>13</th>
                <th style={styleFourteen}>14</th>
                <th style={styleFifteen}>15</th>
              </tr>
              <tr className="parts_row">
              <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(6); setPopupParts(failedSumSix)}}>{failedSumSix}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(7); setPopupParts(failedSumSeven)}}>{failedSumSeven}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(8); setPopupParts(failedSumEight)}}>{failedSumEight}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(9); setPopupParts(failedSumNine)}}>{failedSumNine}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(10); setPopupParts(failedSumTen)}}>{failedSumTen}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(11); setPopupParts(failedSumEleven)}}>{failedSumEleven}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(12); setPopupParts(failedSumTwelve)}}>{failedSumTwelve}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(13); setPopupParts(failedSumThirteen)}}>{failedSumThirteen}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(14); setPopupParts(failedSumFourteen)}}>{failedSumFourteen}</button>
                </th>
                <th>
                  <button className="popup_button" onClick={() => {setPopup(true); setPopupHour(15); setPopupParts(failedSumFifteen)}}>{failedSumFifteen}</button>
                </th>
              </tr>
              <tr>
                <th>{failedSumSix}</th>
                <th>{totalFailedSumSeven}</th>
                <th>{totalFailedSumEight}</th>
                <th>{totalFailedSumNine}</th>
                <th>{totalFailedSumTen}</th>
                <th>{totalFailedSumEleven}</th>
                <th>{totalFailedSumTwelve}</th>
                <th>{totalFailedSumThirteen}</th>
                <th>{totalFailedSumFourteen}</th>
                <th>{totalFailedSumFifteen}</th>
              </tr>
            </table>
          </div>
        </div>
        <Edit hour={popupHour} parts={popupParts} trigger={popup} setTrigger={setPopup} machine={machine}></Edit>
        <div className="graphs">
          <div className="passed_graph">
            <Bar width="460" height="80" data={passedData} options={passedOptions} />
          </div>
          <div className="failed_graph">
            <Bar width="460" height="80" data={failedData} options={failedOptions} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Graph;