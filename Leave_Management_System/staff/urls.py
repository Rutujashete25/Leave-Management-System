from django.urls import path
from .views import LeaveCreateView,LeavesListView,LeavesDetailView,StaffDashboardView,SearchLeavesView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('staff-dashboard/',StaffDashboardView.as_view(), name="staff-dashboard"),
    path('leave-list/', LeavesListView.as_view(), name="leave-list"),
    path('leave-detail/<int:pk>', LeavesDetailView.as_view(), name="leave-detail"),
    path('leave-create/', LeaveCreateView.as_view(), name="leave-create"),
    path('search_leaves/', SearchLeavesView.as_view(), name="search_leaves")


]  +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)