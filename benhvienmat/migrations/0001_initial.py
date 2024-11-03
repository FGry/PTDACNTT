# Generated by Django 5.1.2 on 2024-11-03 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BacSi',
            fields=[
                ('maBacSi', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('soCCCD', models.IntegerField(unique=True)),
                ('hoTenBacSi', models.CharField(max_length=50)),
                ('tuoi', models.IntegerField()),
                ('gioiTinh', models.CharField(choices=[('M', 'Nam'), ('F', 'Nữ')], max_length=5)),
                ('soDienThoai', models.IntegerField()),
                ('diaChi', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BenhNhan',
            fields=[
                ('maBenhNhan', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('soCCCD', models.IntegerField(unique=True)),
                ('maBaoHiemYTe', models.IntegerField(unique=True)),
                ('hoTenBenhNhan', models.CharField(max_length=50)),
                ('tuoi', models.IntegerField()),
                ('gioiTinh', models.CharField(choices=[('M', 'Nam'), ('F', 'Nữ')], max_length=5)),
                ('soDienThoai', models.IntegerField()),
                ('diaChi', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HoSoBenhAn',
            fields=[
                ('thoiGianKham', models.DateTimeField(auto_created=True)),
                ('maBenhAn', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('trieuChung', models.CharField(max_length=255)),
                ('chuanDoan', models.CharField(max_length=255)),
                ('dieuTri', models.CharField(max_length=255)),
                ('benhNhan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='benhvienmat.benhnhan')),
            ],
        ),
    ]
