from rest_framework import generics
from .models import (
    CustomUser, Staff, Announcement, Reply, Accounting, 
    Department, LeaveRequest, Document, Expense, Feedback,Position,
)
from .serializers import (
    PositionSerializer, CustomUserSerializer, StaffSerializer, AnnouncementSerializer,
    ReplySerializer, AccountingSerializer, DepartmentSerializer, LeaveRequestSerializer, DocumentSerializer, ExpenseSerializer, FeedbackSerializer,
)
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Staff, Position, Department, Document, LeaveRequest, Accounting, Expense, Feedback, Announcement, Reply
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
class PositionListCreateView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    
class PositionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class StaffListCreateView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class AnnouncementListCreateView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class AnnouncementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class ReplyListCreateView(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class ReplyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class AccountingListCreateView(generics.ListCreateAPIView):
    queryset = Accounting.objects.all()
    serializer_class = AccountingSerializer

class AccountingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accounting.objects.all()
    serializer_class = AccountingSerializer

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class LeaveRequestListCreateView(generics.ListCreateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

class LeaveRequestRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Permission
from .models import CustomUser  # Ensure this points to your CustomUser model

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate user (DO NOT compare passwords manually)
        user = authenticate(username=username, password=password)

        if user is not None:
            # Serialize user data manually
            user_data = {
                'id': user.id,
                'username': user.username,
                'role': user.role,  # Assuming `role` is a valid field
                'user_permissions': list(user.user_permissions.values_list('codename', flat=True))  # Serialize permissions
            }

            return Response(user_data, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

