from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.


def add_show(request):
    student = User.objects.all() # to show the data from database in front-end
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    return render(request, 'enroll/add_show.html', {'form':fm, 'stu':student})

# Edit and Update Function

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html',{'form':fm})


# Delete Function

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# @login_required(login_url='login')
# def edit_et(request, pk):
#     et = Email_text.objects.get(id=pk)
#     form = ETForm(instance=et)
#     if request.method == "POST":
#         et.et_name = request.POST.get('et_name')
#         et.subject = request.POST.get('subject')
#         et.body = request.POST.get('body')
#         et.save()

#     context = {
#             'form' : form,
#         }
#     return render(request, 'et_form.html', context)

