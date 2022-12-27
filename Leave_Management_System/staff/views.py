from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect,HttpResponseRedirect,render
from accounts.models import  Leaves,CustomUser
from .forms import LeaveApplyForm
from django.db.models import Q
from django.views import View


class StaffDashboardView(View):
    def get(self,request):
        id=self.request.user.id
        user = CustomUser.objects.get(id=id)
        total_leaves=Leaves.objects.filter(Q(user_id=user) & Q(department_id=user.department_id)).count()
        Pending=Leaves.objects.filter(Q(user_id=user) & Q(department_id=user.department_id) & Q(status='Pending')).count()
        Approved=Leaves.objects.filter(Q(user_id=user) & Q(department_id=user.department_id) & Q(status='Approved')).count()
        Rejected=Leaves.objects.filter(Q(user_id=user) & Q(department_id=user.department_id) & Q(status='Rejected')).count()
        context={'total_leaves':total_leaves,'Approved':Approved,'Rejected':Rejected,'Pending':Pending}
        return render(request,'accounts/staff_main_dashboard.html',context)

class LeaveCreateView(LoginRequiredMixin, CreateView):
    model = Leaves
    form_class = LeaveApplyForm
    template_name = 'staff/Leave_form.html'
    success_url = reverse_lazy("leave-list")

    def form_valid(self, form):
        id=self.request.user.id
        dep_id=CustomUser.objects.get(id=id)
        dep=dep_id.department_id
        user = form.save(commit=False)
        user.user_id= self.request.user
        user.department_id = dep
        user.save()


        return super().form_valid(form)


class LeavesListView(LoginRequiredMixin, ListView):
    template_name = 'staff/Leaves_list.html'
    paginate_by = 2

    def get_queryset(self):
        id = self.request.user.id
        dep = CustomUser.objects.get(id=id)
        dep_id = dep.department_id
        queryset =  Leaves.objects.filter(Q(user_id=self.request.user) & Q(department_id=dep_id))
        return queryset

class LeavesDetailView(LoginRequiredMixin, DetailView):
    model = Leaves
    template_name = 'staff/Leaves-detail.html'


class SearchLeavesView(LoginRequiredMixin,View):
    def get(self,request):
        query=request.GET['search']
        page_obj=Leaves.objects.filter(Q(user_id=self.request.user) 
                                        & Q(reason__icontains=query))
        return render(request,'staff/search_list.html',{'page_obj':page_obj})



        



