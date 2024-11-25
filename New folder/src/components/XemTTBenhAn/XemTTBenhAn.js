import React, { useState } from 'react';
import './RecordList.css'; // Nhập file CSS

const RecordList = ({ records }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredRecords, setFilteredRecords] = useState(
    [...records].sort((a, b) => new Date(b.date) - new Date(a.date)) // Sắp xếp giảm dần theo ngày khám
  );
  const [editingRecord, setEditingRecord] = useState(null);

  // Hàm xử lý khi nhấn nút "Tra cứu"
  const handleSearch = () => {
    const results = records
      .filter(
        (record) =>
          record.id.toLowerCase().includes(searchTerm.toLowerCase()) ||
          record.birthDate.includes(searchTerm)
      )
      .sort((a, b) => new Date(b.date) - new Date(a.date)); // Sắp xếp giảm dần theo ngày khám
    setFilteredRecords(results);
  };

  // Hàm xử lý chỉnh sửa
  const handleEdit = (record) => {
    setEditingRecord(record);
  };

  // Hàm xử lý lưu lại sau khi chỉnh sửa
  const handleSave = () => {
    setFilteredRecords((prevRecords) =>
      prevRecords.map((record) =>
        record.id === editingRecord.id ? editingRecord : record
      )
    );
    setEditingRecord(null); // Thoát khỏi chế độ chỉnh sửa
  };

  // Hàm hủy chỉnh sửa
  const handleCancel = () => {
    setEditingRecord(null);
  };

  return (
    <div className="container">
      <h2>Danh Sách Bệnh Án</h2>

      {/* Thanh tìm kiếm */}
      <div className="search-bar">
        <input
          type="text"
          placeholder="Tìm kiếm theo mã bệnh án hoặc ngày sinh (YYYY-MM-DD)"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="search-input"
        />
        <button onClick={handleSearch} className="search-button">
          Tra cứu
        </button>
      </div>

      {/* Danh sách bệnh án */}
      <div className="record-list">
        {filteredRecords.length > 0 ? (
          filteredRecords.map((record) => (
            <div
              key={record.id}
              className="record-item"
              onClick={() => (editingRecord?.id !== record.id ? handleEdit(record) : null)}
            >
              {editingRecord?.id === record.id ? (
                // Chế độ chỉnh sửa
                <div className="edit-mode">
                  <h3>Chỉnh Sửa Bệnh Án: {record.id}</h3>
                  <label>
                    Tên Bệnh Nhân:
                    <input
                      type="text"
                      value={editingRecord.patientName}
                      onChange={(e) =>
                        setEditingRecord({ ...editingRecord, patientName: e.target.value })
                      }
                    />
                  </label>
                  <label>
                    Ngày Sinh:
                    <input
                      type="date"
                      value={editingRecord.birthDate}
                      onChange={(e) =>
                        setEditingRecord({ ...editingRecord, birthDate: e.target.value })
                      }
                    />
                  </label>
                  <label>
                    Ngày Khám:
                    <input
                      type="date"
                      value={editingRecord.date}
                      onChange={(e) =>
                        setEditingRecord({ ...editingRecord, date: e.target.value })
                      }
                    />
                  </label>
                  <label>
                    Chẩn Đoán:
                    <input
                      type="text"
                      value={editingRecord.diagnosis}
                      onChange={(e) =>
                        setEditingRecord({ ...editingRecord, diagnosis: e.target.value })
                      }
                    />
                  </label>
                  <div className="edit-buttons">
                    <button onClick={handleSave} className="edit-button">
                      Lưu
                    </button>
                    <button onClick={handleCancel} className="cancel-button">
                      Hủy
                    </button>
                  </div>
                </div>
              ) : (
                // Hiển thị thông tin bệnh án
                <div>
                  <h3>Bệnh Án: {record.id}</h3>
                  <p><strong>Tên Bệnh Nhân:</strong> {record.patientName}</p>
                  <p><strong>Ngày Sinh:</strong> {record.birthDate}</p>
                  <p><strong>Ngày Khám:</strong> {record.date}</p>
                  <p><strong>Chẩn Đoán:</strong> {record.diagnosis}</p>
                </div>
              )}
            </div>
          ))
        ) : (
          <p>Không tìm thấy bệnh án</p>
        )}
      </div>
    </div>
  );
};

export default RecordList;