import React, { useState } from "react";
import styles from './NhapTTBacSi.module.css';

const NhapTTBacSi = () => {
    const [bacSi, setBacSi] = useState({
        soCCCD: '',
        hoTenBacSi: '',
        tuoi: '',
        gioiTinh: '',
        soDienThoai: '',
        diaChi: '',
    });
    const [hienThi, setHienThi] = useState(false);
    const [thongTinHienThi, setThongTinHienThi] = useState(null);
    let access_token = localStorage.getItem('access_token');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setBacSi({ ...bacSi, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const soDienThoaiRegex = /^0\d{9}$/;
        const soCCCDRegex = /^0\d{11}$/;

        if (!soDienThoaiRegex.test(bacSi.soDienThoai)) {
            alert("Số điện thoại không hợp lệ! (Yêu cầu 10 ký tự bắt đầu bằng 0)");
            return;
        }
        if (!soCCCDRegex.test(bacSi.soCCCD)) {
            alert("Căn cước công dân không hợp lệ! (Yêu cầu 12 ký tự bắt đầu bằng 0)");
            return;
        }

        setThongTinHienThi(bacSi);
        setHienThi(true);
    };

    const handleConfirm = async () => {
        try {
            // Chuyển đổi 'tuoi' từ string thành integer
            const response = await fetch('http://127.0.0.1:8888/api/viewsAPIBacSi/', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${access_token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    soCCCD: bacSi.soCCCD,
                    hoTenBacSi: bacSi.hoTenBacSi,
                    tuoi: parseInt(bacSi.tuoi),  // Chuyển đổi tuổi thành integer
                    gioiTinh: bacSi.gioiTinh,
                    soDienThoai: bacSi.soDienThoai,
                    diaChi: bacSi.diaChi
                }),
            });
            if (response.ok) {
                alert("Thông tin bác sĩ đã được lưu thành công!");
                setBacSi({
                    hoTenBacSi: '',
                    tuoi: '',
                    gioiTinh: '',
                    soDienThoai: '',
                    diaChi: '',
                    soCCCD: '',
                });
                setHienThi(false);
            } else {
                alert("Lỗi khi lưu thông tin bác sĩ.");
            }
        } catch (error) {
            alert("Đã có lỗi xảy ra: " + error.message);
        }
    };

    const closeHienThi = () => {
        setHienThi(!hienThi);
    };

    return (
        <div className={styles.bigdiv}>
            <div className={styles.cont}>
                <h2 style={{ textAlign: 'center', paddingBottom: "20px" }}>Nhập thông tin bác sĩ</h2>
                <form onSubmit={handleSubmit}>
                    <div>
                        <table>
                            <tbody>
                                <tr>
                                    <td><label>Họ và tên:</label></td>
                                    <td>
                                        <input className={styles.in} type="text" name="hoTenBacSi" value={bacSi.hoTenBacSi} onChange={handleChange} required />
                                    </td>
                                </tr>
                                <tr>
                                    <td><label>Tuổi:</label></td>
                                    <td>
                                        <input className={styles.in} type="number" name="tuoi" value={bacSi.tuoi} onChange={handleChange} required />
                                    </td>
                                </tr>
                                <tr>
                                    <td><label>Giới Tính:</label></td>
                                    <td>
                                        <select name="gioiTinh" value={bacSi.gioiTinh} onChange={handleChange} required>
                                            <option value="">Chọn giới tính</option>
                                            <option value="M">Nam</option>
                                            <option value="F">Nữ</option>
                                        </select>
                                    </td>
                                </tr>
                                <tr>
                                    <td><label>Số Điện Thoại:</label></td>
                                    <td>
                                        <input className={styles.in} type="tel" name="soDienThoai" value={bacSi.soDienThoai} onChange={handleChange} required />
                                    </td>
                                </tr>
                                <tr>
                                    <td><label>Địa Chỉ:</label></td>
                                    <td>
                                        <input className={styles.in} type="text" name="diaChi" value={bacSi.diaChi} onChange={handleChange} required />
                                    </td>
                                </tr>
                                <tr>
                                    <td><label>Số Căn Cước Công Dân:</label></td>
                                    <td>
                                        <input className={styles.in} type="text" name="soCCCD" value={bacSi.soCCCD} onChange={handleChange} required maxLength={12} />
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div className={styles.btn_con}><button type="submit" className={styles.btn}>Lưu</button></div>
                </form>
                {hienThi && (
                    <div className={styles.hienThi_nhap}>
                        <div className={styles.hienThi_nhap_content} style={{ marginTop: '20px', border: '1px solid #ccc', padding: '10px', borderRadius: '8px' }}>
                            <div className={styles.header_content}>
                                <h3 style={{ textAlign: "center" }}>Thông tin bác sĩ</h3>
                                <span className={styles.close_btn} onClick={closeHienThi}>&times;</span>
                            </div>
                            <div className={styles.center_content}>
                                <p><strong>Họ và tên:</strong> {thongTinHienThi.hoTenBacSi}</p>
                                <p><strong>Tuổi:</strong> {thongTinHienThi.tuoi}</p>
                                <p><strong>Giới Tính:</strong> {thongTinHienThi.gioiTinh === 'M' ? 'Nam' : 'Nữ'}</p>
                                <p><strong>Số Điện Thoại:</strong> {thongTinHienThi.soDienThoai}</p>
                                <p><strong>Địa Chỉ:</strong> {thongTinHienThi.diaChi}</p>
                                <p><strong>Số Căn Cước Công Dân:</strong> {thongTinHienThi.soCCCD}</p>
                                <button onClick={handleConfirm} className={styles.confirm_btn}>Xác Nhận</button>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default NhapTTBacSi;
