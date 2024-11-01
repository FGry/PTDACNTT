from django.shortcuts import render
from .serializers import BacSiSerializer,BenhNhanSerializer,HoSoBenhAnSerializer
from .models import BacSi,BenhNhan,HoSoBenhAn
# from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

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
    def get(self, request, maBenhNhan = None):
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

    def get(self, request,maBenhAn=None):
        
        if maBenhAn is not None:  # Nếu có id, lấy đối tượng cụ thể
            try:
                ho_so = HoSoBenhAn.objects.get(maBenhAn=maBenhAn)
                serializer = HoSoBenhAnSerializer(ho_so)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except HoSoBenhAn.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
        else:  # Nếu không có id, trả về tất cả
            order = request.query_params.get('order', None) # Lấy tham số 'order' từ query params
            queryset = self.get_queryset()
            # Kiểm tra tham số order
            if order == 'asc':
                queryset = queryset.order_by('thoiGianKham')  # Tăng dần
            elif order == 'desc':
                queryset = queryset.order_by('-thoiGianKham')  # Giảm dần

            serializer = HoSoBenhAnSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
            # http://127.0.0.1:8888/viewsAPIHoso/?order=desc


        

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
