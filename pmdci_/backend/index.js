const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const mysql = require('mysql');
require('dotenv').config();

const db = mysql.createConnection({
    // host: process.env.MYSQL_HOST,
    // user: process.env.MYSQL_USER,
    // password: process.env.MYSQL_PASSWORD,
    // database: process.env.MYSQL_DATABASE,
    host: "localhost",
    user: "root",
    password: "password",
    database: "pmdci_db",
});

// console.log("TESTING: " + process.env.MYSQL_HOST)

db.connect(function(err){
    if(err) throw err;
    console.log("Connected!");
})

app.use(cors());
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/api/getPassedSum/six", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 6";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getPassedSum/seven", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 7";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getPassedSum/eight", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 8";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getPassedSum/nine", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 9";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getPassedSum/ten", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 10";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getPassedSum/eleven", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 11";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getPassedSum/twelve", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 12";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getPassedSum/thirteen", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 13";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getPassedSum/fourteen", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 14";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getPassedSum/fifteen", (req, res) => {
    const sqlSelect = "SELECT SUM(passedCount) AS hourlySum FROM passed_data_entry WHERE HOUR(timestamp) = 15";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getFailedSum/six", (req, res) => {
    const sqlSelect = "SELECT SUM(failedCount) AS hourlySum FROM failed_data_entry WHERE HOUR(timestamp) = 6";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getFailedSum/seven", (req, res) => {
    const sqlSelect = "SELECT SUM(failedCount) AS hourlySum FROM failed_data_entry WHERE HOUR(timestamp) = 7";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getFailedSum/eight", (req, res) => {
    const sqlSelect = "SELECT SUM(failedCount) AS hourlySum FROM failed_data_entry WHERE HOUR(timestamp) = 8";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getFailedSum/nine", (req, res) => {
    const sqlSelect = "SELECT SUM(failedCount) AS hourlySum FROM failed_data_entry WHERE HOUR(timestamp) = 9";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getFailedSum/ten", (req, res) => {
    const sqlSelect = "SELECT SUM(failedCount) AS hourlySum FROM failed_data_entry WHERE HOUR(timestamp) = 10";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getFailedSum/eleven", (req, res) => {
    const sqlSelect = "SELECT SUM(failedCount) AS hourlySum FROM failed_data_entry WHERE HOUR(timestamp) = 11";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getFailedSum/twelve", (req, res) => {
    const sqlSelect = "SELECT SUM(failedCount) AS hourlySum FROM failed_data_entry WHERE HOUR(timestamp) = 12";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getFailedSum/thirteen", (req, res) => {
    const sqlSelect = "SELECT SUM(failedCount) AS hourlySum FROM failed_data_entry WHERE HOUR(timestamp) = 13";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getFailedSum/fourteen", (req, res) => {
    const sqlSelect = "SELECT SUM(failedCount) AS hourlySum FROM failed_data_entry WHERE HOUR(timestamp) = 14";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getFailedSum/fifteen", (req, res) => {
    const sqlSelect = "SELECT SUM(failedCount) AS hourlySum FROM failed_data_entry WHERE HOUR(timestamp) = 15";
    db.query(sqlSelect, (err, result) => {
        res.send(''+result?.[0].hourlySum)
    });
});

app.get("/api/getEngineers", (req, res) => {
    const sqlSelect = "SELECT employeeID FROM pmdci_db.employees WHERE position = 'Process Engineer';";
    db.query(sqlSelect, (err, result) => {
        const engineers = []
        for (let i = 0; i < result.length; i++){
            engineers.push(result[i].employeeID)
        }
        res.send(engineers)
    });
});

app.get("/api/getOperators", (req, res) => {
    const sqlSelect = "SELECT employeeID FROM pmdci_db.employees WHERE position = 'Operator';";
    db.query(sqlSelect, (err, result) => {
        const operators = []
        for (let i = 0; i < result.length; i++){
            operators.push(result[i].employeeID)
        }
        res.send(operators)
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

app.post("/api/edit/passed/6", (req, res) => {
    const passedCount = req.body.passedCount
    const machine = req.body.machine
    const employeeID = req.body.employeeID

    const sqlPassedInsert = `UPDATE passed_data_entry SET passedCount = "${passedCount}", timestamp=timestamp WHERE HOUR(timestamp) = 6;`
    db.query(sqlPassedInsert, [passedCount, machine, employeeID], (err, result) => {
        console.log(err)
    });
});

app.post("/api/edit/passed/7", (req, res) => {
    const passedCount = req.body.passedCount
    const machine = req.body.machine
    const employeeID = req.body.employeeID

    const sqlPassedInsert = `UPDATE passed_data_entry SET passedCount = "${passedCount}", timestamp=timestamp WHERE HOUR(timestamp) = 7;`
    db.query(sqlPassedInsert, [passedCount, machine, employeeID], (err, result) => {
        console.log(err)
    });
});

app.post("/api/edit/passed/8", (req, res) => {
    const passedCount = req.body.passedCount
    const machine = req.body.machine
    const employeeID = req.body.employeeID

    const sqlPassedInsert = `UPDATE passed_data_entry SET passedCount = "${passedCount}", timestamp=timestamp WHERE HOUR(timestamp) = 8;`
    db.query(sqlPassedInsert, [passedCount, machine, employeeID], (err, result) => {
        console.log(err)
    });
});

app.post("/api/edit/passed/9", (req, res) => {
    const passedCount = req.body.passedCount
    const machine = req.body.machine
    const employeeID = req.body.employeeID

    const sqlPassedInsert = `UPDATE passed_data_entry SET passedCount = "${passedCount}", timestamp=timestamp WHERE HOUR(timestamp) = 9;`
    db.query(sqlPassedInsert, [passedCount, machine, employeeID], (err, result) => {
        console.log(err)
    });
});

app.post("/api/edit/passed/10", (req, res) => {
    const passedCount = req.body.passedCount
    const machine = req.body.machine
    const employeeID = req.body.employeeID

    const sqlPassedInsert = `UPDATE passed_data_entry SET passedCount = "${passedCount}", timestamp=timestamp WHERE HOUR(timestamp) = 10;`
    db.query(sqlPassedInsert, [passedCount, machine, employeeID], (err, result) => {
        console.log(err)
    });
});

app.post("/api/edit/passed/11", (req, res) => {
    const passedCount = req.body.passedCount
    const machine = req.body.machine
    const employeeID = req.body.employeeID

    const sqlPassedInsert = `UPDATE passed_data_entry SET passedCount = "${passedCount}", timestamp=timestamp WHERE HOUR(timestamp) = 11;`
    db.query(sqlPassedInsert, [passedCount, machine, employeeID], (err, result) => {
        console.log(err)
    });
});

app.post("/api/edit/passed/12", (req, res) => {
    const passedCount = req.body.passedCount
    const machine = req.body.machine
    const employeeID = req.body.employeeID

    const sqlPassedInsert = `UPDATE passed_data_entry SET passedCount = "${passedCount}", timestamp=timestamp WHERE HOUR(timestamp) = 12;`
    db.query(sqlPassedInsert, [passedCount, machine, employeeID], (err, result) => {
        console.log(err)
    });
});

app.post("/api/edit/passed/13", (req, res) => {
    const passedCount = req.body.passedCount
    const machine = req.body.machine
    const employeeID = req.body.employeeID

    const sqlPassedInsert = `UPDATE passed_data_entry SET passedCount = "${passedCount}", timestamp=timestamp WHERE HOUR(timestamp) = 13;`
    db.query(sqlPassedInsert, [passedCount, machine, employeeID], (err, result) => {
        console.log(err)
    });
});

app.post("/api/edit/passed/14", (req, res) => {
    const passedCount = req.body.passedCount
    const machine = req.body.machine
    const employeeID = req.body.employeeID

    const sqlPassedInsert = `UPDATE passed_data_entry SET passedCount = "${passedCount}", timestamp=timestamp WHERE HOUR(timestamp) = 14;`
    db.query(sqlPassedInsert, [passedCount, machine, employeeID], (err, result) => {
        console.log(err)
    });
});

app.post("/api/edit/passed/15", (req, res) => {
    const passedCount = req.body.passedCount
    const machine = req.body.machine
    const employeeID = req.body.employeeID

    const sqlPassedInsert = `UPDATE passed_data_entry SET passedCount = "${passedCount}", timestamp=timestamp WHERE HOUR(timestamp) = 15;`
    db.query(sqlPassedInsert, [passedCount, machine, employeeID], (err, result) => {
        console.log(err)
    });
});

app.listen(3001, () => {
    console.log("running on port 3001");
});
