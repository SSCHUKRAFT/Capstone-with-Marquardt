const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const mysql = require('mysql');

const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "password",
    database: "pmdci_db",
});

app.use(cors());
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/api/getPassedSum/Machine One", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS passedTotal FROM passed_data_entry WHERE machine = 'Machine One'";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result[0].passedTotal)
    });
});

app.get("/api/getPassedSum/Machine Two", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS passedTotal FROM passed_data_entry WHERE machine = 'Machine Two'";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result[0].passedTotal)
    });
});

app.get("/api/getPassedSum/Machine Three", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS passedTotal FROM passed_data_entry WHERE machine = 'Machine Three'";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result[0].passedTotal)
    });
});

app.get("/api/getPassedSum/six", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 6";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result[0].hourlySum)
    });
});

app.get("/api/getPassedSum/seven", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 7";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result[0].hourlySum)
    });
});

app.get("/api/getPassedSum/eight", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 8";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result[0].hourlySum)
    });
});

app.get("/api/getPassedSum/nine", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 9";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result[0].hourlySum)
    });
});

app.get("/api/getPassedSum/ten", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 10";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result[0].hourlySum)
    });
});

app.get("/api/getPassedSum/eleven", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 11";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result[0].hourlySum)
    });
});

app.get("/api/getPassedSum/twelve", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 12";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result[0].hourlySum)
    });
});

app.get("/api/getPassedSum/thirteen", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 13";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result[0].hourlySum)
    });
});

app.get("/api/getPassedSum/fourteen", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 14";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result[0].hourlySum)
    });
});

app.get("/api/getPassedSum/fifteen", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 15";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result[0].hourlySum)
    });
});

app.get("/api/getPassedSum/twentytwo", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 22";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result[0].hourlySum)
    });
});

app.post("/api/insert/passed", (req, res) => {
    const passedCount = req.body.passedCount
    const machine = req.body.machine
    const employeeID = req.body.employeeID

    const sqlPassedInsert = 
    "INSERT INTO passed_data_entry (passedCount, machine, employeeID) VALUES (?,?,?)"
    db.query(sqlPassedInsert, [passedCount, machine, employeeID], (err, result) => {
        console.log(err)
    });
});

app.post("/api/insert/failed", (req, res) => {
    const failedCount = req.body.failedCount
    const machine = req.body.machine
    const employeeID = req.body.employeeID

    const sqlFailedInsert = 
    "INSERT INTO failed_data_entry (failedCount, machine, employeeID) VALUES (?,?,?)"
    db.query(sqlFailedInsert, [failedCount, machine, employeeID], (err, result) => {
        console.log(err)
    });
});

app.post("/api/insert/retested", (req, res) => {
    const retestedCount = req.body.retestedCount
    const machine = req.body.machine
    const employeeID = req.body.employeeID

    const sqlRetestedInsert = 
    "INSERT INTO retested_data_entry (retestedCount, machine, employeeID) VALUES (?,?,?)"
    db.query(sqlRetestedInsert, [retestedCount, machine, employeeID], (err, result) => {
        console.log(err)
    });
});

app.post("/api/insert/downtime", (req, res) => {
    const downtime = req.body.downtime
    const esclTime = req.body.esclTime
    const errorCode = req.body.errorCode
    const description = req.body.description
    const machine = req.body.machine
    const employeeID = req.body.employeeID

    const sqlDowntimeInsert = 
    "INSERT INTO downtime_data_entry (downtime, esclTime, errorCode, description, machine, employeeID) VALUES (?,?,?,?,?,?)"
    db.query(sqlDowntimeInsert, [downtime, esclTime, errorCode, description, machine, employeeID], (err, result) => {
        console.log(err)
    });
});

app.listen(3001, () => {
    console.log("running on port 3001");
});
