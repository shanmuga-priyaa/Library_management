from django.shortcuts import render,redirect
from django.views import View
from .forms import memberForm
from .models import member

class memberaddView(View):
    def get(self,request):
        data = {"memberForm": memberForm()}
        return render(request,'memberadd.html',data)
    def post(self,request):
        new_data=memberForm(request.POST)
        if new_data.is_valid():
            new_data.save()
            return redirect ('/members/memberlist/')
        
class memberlistView(View):
    def get(self,request):
        data={"memberlist":member.objects.all()}
        print(data)
        return render(request,'memberlist.html',data)
    
class memberdeleteView(View):
    def get(self,request,id):
        selected_data = member.objects.get(id=id)
        selected_data.delete()
        return  redirect ('/members/memberlist/')