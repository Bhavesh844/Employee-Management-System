from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404,FileResponse
from emp.models import emp,Testimonial
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

# @login_required(login_url='/protected_page')
def emp_list(request):
    emps=emp.objects.all() 
    return render(request,'emp/home.html',{'emps':emps})


@login_required(login_url='/protected_page')
def add_emp(request):
    if request.method=='POST':
        emp_name=request.POST.get('emp_name')
        emp_phone=request.POST.get('emp_phone')
        # emp_id=request.POST.get('emp_id')
        emp_work=request.POST.get('emp_work')
        emp_dept=request.POST.get('emp_dept')
        emp_add=request.POST.get('emp_add')
        if emp_work==None:
            emp_work=False
        else:
            emp_work=True
        print(emp_dept)
    
        e=emp(name=emp_name,phone=emp_phone,eid=emp_name[:3]+emp_phone[:3],working=emp_work,department=emp_dept,address=emp_add)
        e.save()
        print(type(e.eid))
        return redirect('/emp/home')

    return render(request,'emp/add_emp.html')
    
@login_required(login_url='/protected_page')
def delete_emp(eid):
    empp=emp.objects.get(pk=eid)
    empp.delete()
    return redirect('/emp/home')
    
@login_required(login_url='/protected_page')
def update_emp(request,eid,):
    if request.user.is_superuser:    
        ee=emp.objects.get(pk=eid)
        return render(request,'emp/update_emp.html',{ 'e':ee})
    return redirect('home')
        
    
@login_required(login_url='/protected_page')
def testimonial(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('Textfield')
        rating=request.POST.get('rating')
        file=request.FILES.get('file')
        T=Testimonial(name=name,desc=desc,file=file,rating=rating)
        T.save()
    return render(request,'testimonial/home.html',{})

@login_required(login_url='/protected_page')
def viewtesti(request):
    li=Testimonial.objects.all()
    # lilist=[i.name for i in li.first()._meta.get_fields()]
    # print(lilist)
    for i in li:
        u=i.file.url
        print(u[u.find('.'):])
    return render(request,'testimonial/viewtesti.html',{'li':li}) 

def download_file(request,pk):  
    testimonial = get_object_or_404(Testimonial, pk=pk)
    file_path = testimonial.file.path
    print(file_path)
    print(file_path[file_path.find('.'):])
    # print(file_path[])
    return FileResponse(testimonial.file, as_attachment=True) 
    
    
