from django.urls import path
from app.views import *
from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('positions/', PositionListCreateView.as_view(), name='position-list-create'),
    path('positions/<int:pk>/', PositionRetrieveUpdateDestroyView.as_view(), name='position-retrieve-update-destroy'),
    path('users/', CustomUserListCreateView.as_view()),
    path('users/<int:pk>/', CustomUserRetrieveUpdateDestroyView.as_view(), name='customuser-retrieve-update-destroy'),
    path('staff/', StaffListCreateView.as_view(), name='staff-list-create'),
    path('staff/<int:pk>/', StaffRetrieveUpdateDestroyView.as_view(), name='staff-retrieve-update-destroy'),
    path('announcements/', AnnouncementListCreateView.as_view(), name='announcement-list-create'),
    path('announcements/<int:pk>/', AnnouncementRetrieveUpdateDestroyView.as_view(), name='announcement-retrieve-update-destroy'),
    path('replies/', ReplyListCreateView.as_view(), name='reply-list-create'),
    path('replies/<int:pk>/', ReplyRetrieveUpdateDestroyView.as_view(), name='reply-retrieve-update-destroy'),
    path('accounting/', AccountingListCreateView.as_view(), name='accounting-list-create'),
    path('accounting/<int:pk>/', AccountingRetrieveUpdateDestroyView.as_view(), name='accounting-retrieve-update-destroy'),
    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroyView.as_view(), name='department-retrieve-update-destroy'),
    path('leave-requests/', LeaveRequestListCreateView.as_view(), name='leave-request-list-create'),
    path('leave-requests/<int:pk>/', LeaveRequestRetrieveUpdateDestroyView.as_view(), name='leave-request-retrieve-update-destroy'),
    path('documents/', DocumentListCreateView.as_view(), name='document-list-create'),
    path('documents/<int:pk>/', DocumentRetrieveUpdateDestroyView.as_view(), name='document-retrieve-update-destroy'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseRetrieveUpdateDestroyView.as_view(), name='expense-retrieve-update-destroy'),
    path('feedbacks/', FeedbackListCreateView.as_view(), name='feedback-list-create'),
    path('feedbacks/<int:pk>/', FeedbackRetrieveUpdateDestroyView.as_view(), name='feedback-retrieve-update-destroy'),
    path('login/', LoginView.as_view(), name='login'),]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
