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

app.post("/api/insert", (req, res) => {
    const passedCount = req.body.passedCount
    const failedCount = req.body.failedCount
    const retestedCount = req.body.retestedCount
    const downtime = req.body.downtime
    const cycletime = req.body.cycletime
    const errorCode = req.body.errorCode
    const downtimeDesc = req.body.downtimeDesc

    const sqlInsert = 
    "INSERT INTO data_entry (passedCount, failedCount, retestedCount, downtime, cycletime, errorCode, downtimeDesc) VALUES (?,?,?,?,?,?,?)"
    db.query(sqlInsert, [passedCount, failedCount, retestedCount, downtime, cycletime, errorCode, downtimeDesc], (err, result) => {
        console.log(err)
    });
});

app.listen(3001, () => {
    console.log("running on port 3001");
});
