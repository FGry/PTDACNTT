from django.db import models
from django.contrib.auth.hashers import make_password

class Patient(models.Model):
    # Thông tin cơ bản của bệnh nhân
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Nam'), ('Female', 'Nữ')])
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.id}"

class MedicalRecord(models.Model):
    # Thông tin bệnh án
    id_ba = models.CharField(max_length=10, primary_key=True)  # Mã bệnh án
    id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')  # Liên kết với bảng Patient
    created_at = models.DateTimeField(auto_now_add=True)  # Lưu thời gian tạo bệnh án (Ngày và giờ)
    symptom = models.CharField(max_length=100)  # Triệu chứng
    diagnosis = models.TextField()  # Chẩn đoán
    treatment = models.TextField()  # Phương pháp điều trị
    
    def __str__(self):
        return f"{self.id_ba} - {self.id.name}"  # Sử dụng self.id để lấy tên bệnh nhân từ bảng Patient


# class Hoso(models.Model):
#     so_cccd = models.CharField(max_length=20, primary_key=True)
#     ten = models.CharField(max_length=50)
#     bhyt = models.CharField(max_length=50, null=True, blank=True)
#     age = models.IntegerField()
#     gioi_tinh = models.CharField(max_length=10)
#     sdt = models.CharField(max_length=20)
#     dia_chi = models.CharField(max_length=50, null=True, blank=True)

#     def __str__(self):
#         return self.so_cccd

# class BenhAn(models.Model):
#     ma_benh_an = models.CharField(max_length=10, primary_key=True)
#     ngay_kham = models.DateField()
#     khoa_dieu_tri = models.CharField(max_length=30)
#     trieu_chung = models.CharField(max_length=100)
#     chuan_doan = models.CharField(max_length=200)
#     dieu_tri = models.CharField(max_length=100)
#     so_cccd = models.ForeignKey(Hoso, on_delete=models.CASCADE, to_field='so_cccd')

#     def __str__(self):
#         return f"{self.ma_benh_an} - {self.chuan_doan}"

