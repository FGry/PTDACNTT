import React, { useState } from "react";
import styles from './NhapTTBacSi.module.css';

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
    const [errors, setErrors] = useState({
        dob: '',
        phone: '',
        cIN: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setBacSi({ ...bacSi, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const phoneRegex = /^0\d{9}$/;
        const cINRegex = /^0\d{11}$/;
        const today = new Date();
        const dob = new Date(bacSi.dob);
        let errorMessages = {};

        if (dob >= today) {
            errorMessages.dob = "Ngày sinh không hợp lệ";
        }
        if (!phoneRegex.test(bacSi.phone)) {
            errorMessages.phone = "Số điện thoại không hợp lệ! (Yêu cầu 10 ký tự bắt đầu bằng 0)";
        }
        if (!cINRegex.test(bacSi.cIN)) {
            errorMessages.cIN = "Căn cước công dân không hợp lệ! (Yêu cầu 12 ký tự bắt đầu bằng 0)";
        }

        // Nếu có lỗi, set lại state errorMessages
        if (Object.keys(errorMessages).length > 0) {
            setErrors(errorMessages);
            return;
        }

        setThongTinHienThi(bacSi);
        setHienThi(true);
        setErrors({}); // Reset lỗi khi form hợp lệ
    };

    const closeHienThi = () => {
        setHienThi(!hienThi);
    };

    const handleConfirm = async () => {
        // setLoading(true); // Start loading

        // // Send data to the server using fetch or axios
        // try {
        //     const response = await fetch('http://yourapiendpoint.com/api/benhnhan', {
        //         method: 'POST',
        //         headers: {
        //             'Content-Type': 'application/json',
        //         },
        //         body: JSON.stringify(benhNhan), // Send the data in the request body
        //     });

        //     if (response.ok) {
        //         const result = await response.json();
        //         setSuccessMessage("Dữ liệu đã được lưu thành công!");
        //         setThongTinHienThi(null); // Clear the displayed info
        //         setBenhNhan({
        //             name: '',
        //             dob: '',
        //             gender: '',
        //             ethnic: '',
        //             phone: '',
        //             address: '',
        //             cIN: '',
        //             hIN: '',
        //         }); // Reset the form
        //     } else {
        //         setSuccessMessage("Có lỗi xảy ra. Vui lòng thử lại.");
        //     }
        // } catch (error) {
        //     setSuccessMessage("Có lỗi xảy ra. Vui lòng thử lại.");
        // } finally {
        //     setLoading(false); // Stop loading
        // }
    };

    return (
        <div className={styles.bigdiv}>
            <div className={styles.cont}>
                <h2 style={{ textAlign: 'center', paddingBottom:"20px" }}>Nhập thông tin bác sĩ</h2>
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
                                        {errors.dob && <span className={styles.error}>{errors.dob}</span>}
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
                                        {errors.phone && <span className={styles.error}>{errors.phone}</span>}
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
                                        {errors.cIN && <span className={styles.error}>{errors.cIN}</span>}
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
                                <button className={styles.btn} onClick={handleConfirm}>Xác nhận</button>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default NhapTTBacSi;
