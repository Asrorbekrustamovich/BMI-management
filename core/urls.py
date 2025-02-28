from django.urls import path
from app.views import *
from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static
from django.http import JsonResponse

def healthcheck(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('health/', healthcheck),
]

urlpatterns = [
    path()
    path('admin/', admin.site.urls),
    path('users/', CustomUserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', CustomUserDetail.as_view(), name='user-detail'),

    # Role URLs
    path('roles/', RoleListCreate.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', RoleDetail.as_view(), name='role-detail'),

    # Department URLs
    path('departments/', DepartmentListCreate.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentDetail.as_view(), name='department-detail'),

    # Position URLs
    path('positions/', PositionListCreate.as_view(), name='position-list-create'),
    path('positions/<int:pk>/', PositionDetail.as_view(), name='position-detail'),

    # Staff URLs
    path('staff/', StaffListCreate.as_view(), name='staff-list-create'),
    path('staff/<int:pk>/', StaffDetail.as_view(), name='staff-detail'),

    # Announcement URLs
    path('announcements/', AnnouncementListCreate.as_view(), name='announcement-list-create'),
    path('announcements/<int:pk>/', AnnouncementDetail.as_view(), name='announcement-detail'),

    # Accounting URLs
    path('accounting/', AccountingListCreate.as_view(), name='accounting-list-create'),
    path('accounting/<int:pk>/', AccountingDetail.as_view(), name='accounting-detail'),

    # LeaveRequest URLs
    path('leave-requests/', LeaveRequestListCreate.as_view(), name='leave-request-list-create'),
    path('leave-requests/<int:pk>/', LeaveRequestDetail.as_view(), name='leave-request-detail'),

    # Document URLs
    path('documents/', DocumentListCreate.as_view(), name='document-list-create'),
    path('documents/<int:pk>/', DocumentDetail.as_view(), name='document-detail'),

    # Expense URLs
    path('expenses/', ExpenseListCreate.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetail.as_view(), name='expense-detail'),

    # Message URLs
    path('messages/', MessageListCreate.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageDetail.as_view(), name='message-detail'),

    # Login URL
    path('login/', LoginView.as_view(), name='login'),]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

