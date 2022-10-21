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

app.get("/api/get", (req, res) => {
    const sqlSelect = "SELECT * FROM data_entry";
    db.query(sqlSelect, (err, result) => {
        res.send(result)
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
