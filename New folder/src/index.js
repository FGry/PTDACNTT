import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
// import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// import NhapTTBenhNhan from "./components/NhapTTBenhNhan/NhapTTBenhNhan";
// import NhapTTBenhAn from "./components/NhapTTBenhAn/NhapTTBenhAn";
// import NhapTTBacSi from "./components/NhapTTBacSi/NhapTTBacSi";
// import MainGUI from './components/GUI/MainGUI';
// import DangNhap from './components/DangNhap/DangNhap'
// import ProtectedRoute from './sevices/ProtectedRoute';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
            // <Router>
            //       <App />
            //       <Routes>
            //             <ProtectedRoute path='/nhapTTBenhNhan' element={<NhapTTBenhNhan />} />
            //             <ProtectedRoute path='/nhapTTBenhAn' element={<NhapTTBenhAn />} />
            //             <ProtectedRoute path='/nhapTTBacSi' element={<NhapTTBacSi />} />
            //             <Route path='/' element={<MainGUI />} />
            //             <Route path='/dangNhap' element={<DangNhap />} />
            //       </Routes>
            // </Router>
            <App/>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals


