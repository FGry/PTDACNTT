import React, {useState} from "react";
import styles from './NhapTTBacSi.module.css'

const NhapTTBacSi = () => {
    const [bacSi, setBacSi] = useState({
        name: '',
        dob: '',
        gender: '',
        phone: '',
        address: '',
        cIN: '',
    });
    const [hienThi, setHienThi] = useState(false);
    const [thongTinHienThi, setThongTinHienThi] = useState(null);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setBacSi({ ...bacSi, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const phoneRegex = /^0\d{9}$/;
        const cINRegex = /^0\d{11}$/;
        const todayString = (new Date()).toISOString().split('T')[0];

        if (bacSi.dob >= todayString){
            alert("Ngày sinh không hợp lệ");
            return;

        }else if (!phoneRegex.test(bacSi.phone)) {
            alert("Số điện thoại không hợp lệ! (Yêu cầu 10 ký tự bắt đầu bằng 0)");
            return;
        }else if (!cINRegex.test(bacSi.cIN)) {
            alert("Căn cước công dân không hợp lệ! (Yêu cầu 12 ký tự bắt đầu bằng 0)");
            return;
        }
        setThongTinHienThi(bacSi);
        setHienThi(true);
    };    


    const handleChangeCheckBox = () => {
        setIsChecked(!isChecked);
    };

    const [isChecked, setIsChecked] = useState(false);
    const closeHienThi = () => {
        setHienThi(!hienThi);
    };

    return (
        <div className={styles.cont} >
            <h3 style={{ textAlign: 'center' }}>Nhập thông tin bác sĩ</h3>
            <form onSubmit={handleSubmit}>
                <div>
                    <table>
                        <tbody>
                            <tr>
                                <td><label>Họ và tên:</label></td>
                                <td>
                                    <input className={styles.in} type="text" name="name" value={bacSi.name} onChange={handleChange} required />
                                </td>
                            </tr>
                            <tr>
                                <td><label>Ngày tháng năm sinh:</label></td>
                                <td>
                                    <input type="date" name='dob' value={bacSi.dob} onChange={handleChange} required />
                                </td>
                            </tr>
                            <tr>
                                <td><label>Giới Tính:</label></td>
                                <td>
                                    <select name="gender" value={bacSi.gender} onChange={handleChange} required>
                                        <option value="">Chọn giới tính</option>
                                        <option value="nam">Nam</option>
                                        <option value="nữ">Nữ</option>
                                        <option value="khác">Khác</option>
                                    </select>
                                </td>
                            </tr>
                            <tr>
                                <td><label>Số Điện Thoại:</label></td>
                                <td>
                                    <input className={styles.in} type="tel" name="phone" value={bacSi.phone} onChange={handleChange} required />
                                </td>
                            </tr>
                            <tr>
                                <td><label>Địa Chỉ:</label></td>
                                <td>
                                    <input className={styles.in} type="text" name="address" value={bacSi.address} onChange={handleChange} required />
                                </td>
                            </tr>
                            <tr>
                                <td><label>Số Căn Cước Công Dân:</label></td>
                                <td>
                                    <input className={styles.in} type="text" name="cIN" value={bacSi.cIN} onChange={handleChange} required maxLength={12} />
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
                            <p><strong>Họ và tên:</strong> {thongTinHienThi.name}</p>
                            <p><strong>Ngày tháng năm sinh:</strong> {thongTinHienThi.dob}</p>
                            <p><strong>Giới Tính:</strong> {thongTinHienThi.gender}</p>
                            <p><strong>Số Điện Thoại:</strong> {thongTinHienThi.phone}</p>
                            <p><strong>Địa Chỉ:</strong> {thongTinHienThi.address}</p>
                        </div>
                        <div className={styles.btn_con}>
                            <button className={styles.btn} onClick={closeHienThi}>Hủy</button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default NhapTTBacSi;