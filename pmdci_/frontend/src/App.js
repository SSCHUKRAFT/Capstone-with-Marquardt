import './App.css'
import React from "react";
import { DataEntry } from './pages/data_entry';
import { Signin } from './pages/sign_in';
import { Engineer } from './pages/engineer';
import { BrowserRouter as Router, Routes, Route, Navigate} from 'react-router-dom';

function App() {
  return(
    <Router>
      <Routes>
        <Route path = "/" element={<Signin/>} />
        <Route path = "/data-entry" element={<DataEntry/>} />
        <Route path = "/engineer" element={<Engineer/>} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
}

export default App