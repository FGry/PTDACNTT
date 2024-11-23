from django.shortcuts import render
from .serializers import BacSiSerializer,BenhNhanSerializer,HoSoBenhAnSerializer
from .models import BacSi,BenhNhan,HoSoBenhAn
# from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime

import requests #pip install requests , thu vien tra ve api tren http


# render ra view

class GetBacSiAPI(APIView):
    def get_queryset(self):
        # Điều này đảm bảo mỗi request đều gọi lại database,
        # đảm bảo dữ liệu không bị cache và luôn phản ánh chính xác dữ liệu trong cơ sở dữ liệu hiện tại.
        return BacSi.objects.all()


    def get(self,request, maBacSi = None):
        if (maBacSi is not None):  # Nếu có id, lấy đối tượng cụ thể
            try:
                bac_si = BacSi.objects.get(maBacSi=maBacSi)
                serializer = BacSiSerializer(bac_si)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except BacSi.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:  # Nếu không có id, trả về tất cả
            bacsi = self.get_queryset()
            serializer = BacSiSerializer(bacsi,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BacSiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # update Data
    def put(self, request, maBacSi):
        try:
            bac_si = BacSi.objects.get(maBacSi=maBacSi)
        except BacSi.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BacSiSerializer(bac_si, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #delete data
    def delete(self, request, maBacSi):
        try:
            bac_si = BacSi.objects.get(maBacSi=maBacSi)
        except BacSi.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        bac_si.delete()
        return Response("Da xoa thanh cong",status=status.HTTP_204_NO_CONTENT)
    

class BenhNhanAPI(APIView):
    # get info
    def get_queryset(self):
        return BenhNhan.objects.all()

    # get all infor
    def get(self, request):

        maBenhNhan = request.query_params.get('maBenhNhan', None)

        if maBenhNhan is not None:  # Nếu có id, lấy đối tượng cụ thể
            try:
                benh_nhan = BenhNhan.objects.get(maBenhNhan=maBenhNhan)
                serializer = BenhNhanSerializer(benh_nhan)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except BenhNhan.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:  # Nếu không có id, trả về tất cả
            queryset = self.get_queryset()
            serializer = BenhNhanSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # create data
    def post(self, request):
        serializer = BenhNhanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # update Data
    def put(self, request, maBenhNhan):
        try:
            benh_nhan = BenhNhan.objects.get(maBenhNhan=maBenhNhan)
        except BenhNhan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BenhNhanSerializer(benh_nhan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #delete data
    def delete(self, request, maBenhNhan):
        try:
            benh_nhan = BenhNhan.objects.get(maBenhNhan=maBenhNhan)
        except BenhNhan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        benh_nhan.delete()
        return Response("Da xoa thanh cong",status=status.HTTP_204_NO_CONTENT)
    



    
class HoSoBenhAnAPI(APIView):

    def get_queryset(self):
        return HoSoBenhAn.objects.all()

    def get(self, request):
        
        maBenhAn = request.query_params.get('maBenhAn', None)
        maBenhNhan = request.query_params.get('maBenhNhan', None)
        ngay = request.query_params.get('ngay', None)  

        if maBenhAn is not None:  # Nếu có id, lấy đối tượng cụ thể
            try:
                ho_so = HoSoBenhAn.objects.get(maBenhAn=maBenhAn)
                serializer = HoSoBenhAnSerializer(ho_so)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except HoSoBenhAn.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)            
        elif maBenhNhan is not None:  # Nếu có id, lấy đối tượng cụ thể 
            try:
                # Lấy thông tin bệnh nhân
                benh_nhan = BenhNhan.objects.get(maBenhNhan=maBenhNhan)
                
                # Lấy tất cả hồ sơ bệnh án của bệnh nhân này
                ho_so = HoSoBenhAn.objects.filter(benhNhan=benh_nhan)
                
                # Sử dụng serializer để trả về thông tin bệnh nhân và hồ sơ bệnh án
                benh_nhan_data = {
                    "maBenhNhan": benh_nhan.maBenhNhan,
                    "hoTenBenhNhan": benh_nhan.hoTenBenhNhan,
                    "hoSoBenhAn": HoSoBenhAnSerializer(ho_so, many=True).data  # Danh sách hồ sơ bệnh án
                }
                
                return Response(benh_nhan_data, status=status.HTTP_200_OK)
            except BenhNhan.DoesNotExist:
                return Response({"error": "Không tìm thấy bệnh nhân"}, status=status.HTTP_404_NOT_FOUND)
        elif ngay is not None:
            try:
                # Định dạng ngày:  format 'YYYY-MM-DD'
                ngay_kham = datetime.strptime(ngay, '%Y-%m-%d').date()
                print(ngay_kham) #ktra ngay trong terminal
                # Lọc hồ sơ theo ngày khám
                queryset = HoSoBenhAn.objects.filter(thoiGianKham__date=ngay_kham)
                
                serializer = HoSoBenhAnSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ValueError:
                return Response({"error": "Định dạng ngày không hợp lệ. Định dạng đúng: YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)

        else:  
            order = request.query_params.get('order', None) # Lấy tham số 'order' từ query params
            queryset = self.get_queryset()
            
            if order == 'asc':
                queryset = queryset.order_by('thoiGianKham')  # Tăng dần
            elif order == 'desc':
                queryset = queryset.order_by('-thoiGianKham')  # Giảm dần

            serializer = HoSoBenhAnSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

    def post(self, request):
        serializer = HoSoBenhAnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # update Data
    def put(self, request, maBenhAn):
        try:
            ho_so = HoSoBenhAn.objects.get(maBenhAn=maBenhAn)
        except HoSoBenhAn.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = HoSoBenhAnSerializer(ho_so, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #delete data
    def delete(self, request, maBenhAn):
        try:
            ho_so = HoSoBenhAn.objects.get(maBenhAn=maBenhAn)
        except HoSoBenhAn.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        ho_so.delete()
        return Response("Da xoa thanh cong",status=status.HTTP_204_NO_CONTENT)


def ho_so_benh_an_theo_ngay(request):
    # Lấy ngày từ tham số query
    ngay = request.GET.get('ngay')

    # Nếu có tham số ngày, gọi API để lấy dữ liệu
    if ngay:
        # Thay đổi đường dẫn API theo đúng URL của bạn
        api_url = f'http://127.0.0.1:8888/api/viewsAPIHoSo/?ngay={ngay}'
        response = requests.get(api_url)

        # Kiểm tra nếu API trả về dữ liệu thành công
        if response.status_code == 200:
            ho_so_benh_an_date = response.json()  # Lấy dữ liệu JSON từ response
        else:
            ho_so_benh_an_date = []  # Nếu không có dữ liệu, để danh sách rỗng
    else:
        ho_so_benh_an_date = []

    # Render dữ liệu vào template
    return render(request, 'ho_so_benh_an_date.html', {'ho_so_benh_an_date': ho_so_benh_an_date, 'ngay': ngay})



def danh_sach_hoso_view(request):

    # Lấy ngày từ tham số query
    order = request.GET.get('order', 'desc')  # Mặc định là 'desc' nếu không có order

    # Nếu có tham số ngày, gọi API để lấy dữ liệu
    if order:
        # Thay đổi đường dẫn API theo đúng URL của bạn
        api_url = f'http://127.0.0.1:8888/api/viewsAPIHoSo/?order={order}'
        response = requests.get(api_url)

        # Kiểm tra nếu API trả về dữ liệu thành công
        if response.status_code == 200:
            ho_so_benh_an = response.json()  # Lấy dữ liệu JSON từ response
        else:
            ho_so_benh_an = []  # Nếu không có dữ liệu, để danh sách rỗng
    else:
        ho_so_benh_an = []

    # Render dữ liệu vào template
    return render(request, 'ho_so_benh_an.html', {'ho_so_benh_an': ho_so_benh_an, 'order': order})

from django.utils.dateparse import parse_date
# khoang ngay

def ho_so_benh_an_theo_khoang_ngay(request):
    ngay_bat_dau = request.GET.get('ngay_bat_dau')
    ngay_ket_thuc = request.GET.get('ngay_ket_thuc')
    ho_so_benh_an = []

    if ngay_bat_dau and ngay_ket_thuc:
        # Chuyển đổi chuỗi sang đối tượng datetime
        ngay_bat_dau = parse_date(ngay_bat_dau)
        ngay_ket_thuc = parse_date(ngay_ket_thuc)

        # Lọc hồ sơ theo khoảng thời gian
        ho_so_benh_an = HoSoBenhAn.objects.filter(
            thoiGianKham__date__gte=ngay_bat_dau,
            thoiGianKham__date__lte=ngay_ket_thuc
        )

    context = {
        'ho_so_benh_an': ho_so_benh_an,
        'ngay_bat_dau': ngay_bat_dau,
        'ngay_ket_thuc': ngay_ket_thuc
    }
    return render(request, 'ho_so_khoang_ngay.html', context)