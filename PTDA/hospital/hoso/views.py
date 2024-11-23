from .models import Patient, MedicalRecord
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PatientSerializer 
from .serializers import MedicalRecordSerializer
from rest_framework import status
from rest_framework.exceptions import ValidationError



class DanhSachHosoView(APIView):
    def get(self, request):
        # Lấy danh sách hồ sơ từ database
        danh_sach_hs = Patient.objects.all()
        
        # Sử dụng serializer để chuyển đổi dữ liệu thành định dạng JSON
        serializer = PatientSerializer(danh_sach_hs, many=True)
        
        # Trả về dữ liệu dưới dạng JSON
        return Response({'danh_sach_hs': serializer.data}, status=200)






class DanhSachBenhAnView(APIView):
    def get(self, request):
        # Lấy tất cả các bệnh án
        benh_an_list = MedicalRecord.objects.all().order_by('-created_at')  # Sắp xếp theo ngày khám mới nhất
        
        # Nếu bạn muốn lọc theo số CCCD thì dùng đoạn mã dưới
        # so_cccd = request.GET.get('so_cccd', None)
        # if so_cccd:
        #     benh_an_list = benh_an_list.filter(so_cccd__so_cccd=so_cccd)

        # Serialize dữ liệu để trả về
        serializer = MedicalRecordSerializer(benh_an_list, many=True)
        return Response({'benh_an': serializer.data}, status=status.HTTP_200_OK)
    
    
class ThemHosoView(APIView):
#     {
#     "id": "1234567890",
#     "name": "Nguyen Van A",
#     "date_of_birth": "1990-01-01",
#     "gender": "Male",
#     "phone_number": "0123456789",
#     "address": "123 ABC Street, Hanoi"
# }

    def post(self, request):
        # In ra dữ liệu nhận được để kiểm tra
        print("Received data:", request.data)
        
        # Chuyển dữ liệu từ request thành serializer để kiểm tra tính hợp lệ
        serializer = PatientSerializer(data=request.data)
        
        if serializer.is_valid():
            # Nếu dữ liệu hợp lệ, lưu hồ sơ và trả về phản hồi thành công
            serializer.save()
            return Response({'message': 'Lưu hồ sơ thành công!'}, status=status.HTTP_201_CREATED)
        else:
            # Nếu dữ liệu không hợp lệ, trả về lỗi
            print("Validation errors:", serializer.errors)
            raise ValidationError({'errors': serializer.errors})





# views.py

class ThemBenhAnView(APIView):
#     {
#     "id_ba": "BA123456",
#     "id": "1234567890",
#     "symptom": "Cảm cúm",
#     "diagnosis": "Viêm đường hô hấp trên",
#     "treatment": "Uống thuốc cảm",
#     "created_at": "2024-11-23"
# }

    def post(self, request):
        # Lấy dữ liệu từ request
        data = request.data

        # Kiểm tra xem bệnh nhân có tồn tại không
        try:
            patient = Patient.objects.get(id=data['id'])
        except Patient.DoesNotExist:
            raise ValidationError("Bệnh nhân không tồn tại!")

        # Kiểm tra nếu mã bệnh án đã tồn tại
        if MedicalRecord.objects.filter(id_ba=data['id_ba']).exists():
            return Response({"detail": "Mã bệnh án đã tồn tại!"}, status=status.HTTP_400_BAD_REQUEST)

        # Khởi tạo serializer với dữ liệu
        serializer = MedicalRecordSerializer(data=data)

        # Kiểm tra xem serializer có hợp lệ không
        if serializer.is_valid():
            # Lưu bệnh án và liên kết với bệnh nhân
            serializer.save(id=patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TimKiemCCCDView(APIView):
    # http://127.0.0.1:8000/api/hoso/timkiem/?id=111
    def get(self, request):
        # Lấy số CCCD từ tham số GET
        search = request.GET.get('id', None)
        patient = None
        benh_an_list = []

        # Kiểm tra nếu số CCCD có được truyền vào không
        if search:
            # Tìm hồ sơ bệnh nhân dựa trên số CCCD
            patient = Patient.objects.filter(id=search).first()
            if patient:
                # Lấy danh sách bệnh án của bệnh nhân từ số CCCD
                benh_an_list = MedicalRecord.objects.filter(id=patient).order_by('-created_at')

        # Serialize dữ liệu hồ sơ và danh sách bệnh án
        patient_data = PatientSerializer(patient).data if patient else None
        benh_an_data = MedicalRecordSerializer(benh_an_list, many=True).data

        # Trả về kết quả dưới dạng JSON
        return Response({
            'patient': patient_data,
            'benh_an_list': benh_an_data,
            'search': search
        }, status=status.HTTP_200_OK)

from .forms import FilterBenhAnForm  # Import form nếu cần sử dụng trong view
class LocBenhAnView(APIView):
    # http://127.0.0.1:8000/api/hoso/loc/?start_date=2024-01-01&end_date=2024-11-23
    def get(self, request):
        # Lấy dữ liệu từ GET request
        form = FilterBenhAnForm(request.GET)

        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            
            # Lọc bệnh án theo khoảng thời gian
            danh_sach_benh_an = MedicalRecord.objects.filter(created_at__range=(start_date, end_date)).order_by('-created_at')
            
            # Serialize dữ liệu bệnh án
            benh_an_data = MedicalRecordSerializer(danh_sach_benh_an, many=True).data

            return Response({
                'danh_sach_benh_an': benh_an_data
            }, status=status.HTTP_200_OK)

        return Response({
            'errors': form.errors
        }, status=status.HTTP_400_BAD_REQUEST)
