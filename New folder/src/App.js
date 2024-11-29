// import React from "react";
// import './menu.css'
// import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
// import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// import NhapTTBenhNhan from "./components/NhapTTBenhNhan/NhapTTBenhNhan";
// import NhapTTBenhAn from "./components/NhapTTBenhAn/NhapTTBenhAn";
// import NhapTTBacSi from "./components/NhapTTBacSi/NhapTTBacSi";
// import MainGUI from './components/GUI/MainGUI';
// import DangNhap from './components/DangNhap/DangNhap'
// import ProtectedRoute from './sevices/ProtectedRoute';

// function App() {
//   return (
//     <nav>
//       <div className="logo">
//         <img src="/asset/anh3.png" alt="logo" />
//       </div>
//       <div className="menu">
//         <ul>
//           <li><Link to='/'>Trang chủ</Link></li>
//           <li><Link to="/nhapTTBenhNhan">Bệnh Nhân</Link></li>
//           <li><Link to="/nhapTTBacSi">Bác sĩ</Link></li>
//           <li><Link to='/nhapTTBenhAn'>Bệnh án</Link></li>
//         </ul>
//       </div>
//       <div className="timKiem">
//         <input type="search" id="timKiemInput" placeholder="Nhập mã bệnh án để tra cứu..." />
//         <button type="button" id="timKiemButton">Tìm Kiếm</button>
//       </div>
//       <div>
//         <li><Link to='/dangNhap'>Bệnh án</Link></li>
//       </div>
//     </nav>
//   );
// }

// export default App;

import React from "react";
import './menu.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import NhapTTBenhNhan from "./components/NhapTTBenhNhan/NhapTTBenhNhan";
import NhapTTBenhAn from "./components/NhapTTBenhAn/NhapTTBenhAn";
import NhapTTBacSi from "./components/NhapTTBacSi/NhapTTBacSi";
import MainGUI from './components/GUI/MainGUI';
import DangNhap from './components/DangNhap/DangNhap';
import DangXuat from "./components/DangXuat/DangXuat";
import ProtectedRoute from './sevices/ProtectedRoute';

function App() {

  const token = localStorage.getItem('access_token')

  return (
    <Router>
      <nav>
        <div className="logo">
          <img src="/asset/anh3.png" alt="logo" />
        </div>
        <div className="menu">
          <ul>
            <li><Link to='/'>Trang chủ</Link></li>
            <li><Link to="/nhapTTBenhNhan">Bệnh Nhân</Link></li>
            <li><Link to="/nhapTTBacSi">Bác sĩ</Link></li>
            <li><Link to='/nhapTTBenhAn'>Bệnh án</Link></li>
          </ul>
        </div>
        <div className="timKiem">
          <input type="search" id="timKiemInput" placeholder="Nhập mã bệnh án để tra cứu..." />
          <button type="button" id="timKiemButton">Tìm Kiếm</button>
        </div>
        <div className="menu">
          <ul>
            {token ? (
              <li><Link to='/dangXuat'>Đăng Xuất</Link></li>
            ) : (
              <li><Link to='/dangNhap'>Đăng Nhập</Link></li>
            )}
          </ul>
        </div>
      </nav>

      {/* Định nghĩa các routes */}
      <Routes>
        <Route path="/" element={<MainGUI />} />
        <Route path="/dangNhap" element={<DangNhap />} />

        {/* Sử dụng ProtectedRoute để bảo vệ các route */}
        <Route
          path="/nhapTTBenhNhan"
          element={<ProtectedRoute element={<NhapTTBenhNhan />} />}
        />
        <Route
          path="/nhapTTBenhAn"
          element={<ProtectedRoute element={<NhapTTBenhAn />} />}
        />
        <Route
          path="/nhapTTBacSi"
          element={<ProtectedRoute element={<NhapTTBacSi />} />}
        />

        <Route
          path="/dangXuat"
          element={<ProtectedRoute element={<DangXuat />} />}
        />
      </Routes>
    </Router>
  );
}

export default App;

