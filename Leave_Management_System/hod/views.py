from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect,HttpResponseRedirect,render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.hashers import make_password
from accounts.models import CustomUser,Role,Leaves
from .forms import StaffRegistartionForm
from django.db.models import Q

class HodDashboardView(View):
    def get(self,request):
        id=self.request.user.id
        user = CustomUser.objects.get(id=id)
        staff_count=CustomUser.objects.filter(Q(role_id__id=2) & Q(department_id=user.department_id)).count()
        context={'staff_count':staff_count}
        return render(request,'accounts/hoddashboard.html',context)


class StaffCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    form_class = StaffRegistartionForm
    template_name = 'hod/staff_form.html'
    success_url = reverse_lazy("staff-list")

    def form_valid(self, form):
        id=self.request.user.id
        user_name=CustomUser.objects.get(id=id)
        user = form.save(commit=False)
        auto_pass = self.request.POST.get('name').capitalize()+'@'+'1234'
        hash_pass = make_password(auto_pass)
        user.password = hash_pass
        user.role_id= Role.objects.get(pk=2)
        user.department_id = user_name.department_id
        user.save()
        return super().form_valid(form)


class StaffListView(LoginRequiredMixin, ListView):
    template_name = 'hod/staff_list.html'
    paginate_by = 5

    def get_queryset(self):
        id = self.request.user.id
        user = CustomUser.objects.get(id=id)
        queryset = CustomUser.objects.filter(
            Q(role_id__id=2) & Q(department_id=user.department_id))
        return queryset

class StaffDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'hod/staff_confirm_delete.html'
    success_url = reverse_lazy('staff-list')

class StaffDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'hod/staff-detail.html'


class StaffLeaveView(LoginRequiredMixin, ListView):
    paginate_by = 5
    template_name = 'hod/staff_leaves.html'

    def get_queryset(self):
        id = self.request.user.id
        user = CustomUser.objects.get(id=id)
        queryset = Leaves.objects.filter(Q(department_id=user.department_id))
        return queryset

class UpdateStatusView(View):
    def post(self,request,id):
        leave_obj = Leaves.objects.get(id=id)
        leave_obj.status = request.POST.get('status')
        leave_obj.save()
        return redirect('staff-leaves')
        
class SearchStaffListView(LoginRequiredMixin,View):
    def get(self,request):
        id=self.request.user.id
        user = CustomUser.objects.get(id=id)
        query=request.GET['search']
        page_obj=CustomUser.objects.filter(Q(department_id=user.department_id) & Q(role_id__id=2)
                                        & Q(name__icontains=query))
        return render(request,'hod/search_staff_list.html',{'page_obj':page_obj})


class SearchStaffLeaveView(LoginRequiredMixin,View):
    def get(self,request):
        id=self.request.user.id
        user = CustomUser.objects.get(id=id)
        query=request.GET['search']
        page_obj=Leaves.objects.filter(Q(department_id=user.department_id) 
                                         & Q(user_id__name__icontains=query))
        return render(request,'hod/search_staff_leave.html',{'page_obj':page_obj})



