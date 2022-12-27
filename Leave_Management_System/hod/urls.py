from django.urls import path
from .views import SearchStaffLeaveView,SearchStaffListView,StaffListView ,StaffDeleteView, StaffDetailView ,StaffCreateView,StaffLeaveView,HodDashboardView, UpdateStatusView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('hod-dashboard/',HodDashboardView.as_view(), name="hod-dashboard"),
    path('staff-list/', StaffListView.as_view(), name="staff-list"),
    path('staff-delete/<int:pk>', StaffDeleteView.as_view(), name="staff-delete"),
    path('staff-detail/<int:pk>', StaffDetailView.as_view(), name="staff-detail"),
    path('staff-create/', StaffCreateView.as_view(), name="staff-create"),
    path('staff-leaves/', StaffLeaveView.as_view(), name="staff-leaves"),
    path('update-status/<int:id>/', UpdateStatusView.as_view(), name="update-status"),
    path('search-staff-list/', SearchStaffListView.as_view(), name="search-staff-list"),
    path('search-staff-leave/', SearchStaffLeaveView.as_view(), name="search-staff-leave"),



]  +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)