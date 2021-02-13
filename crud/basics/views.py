from django.shortcuts import render
#from django.views.generic.edit import CreateView
from .models import Student
#from django.views.generic import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic import UpdateView
#from django.views.generic.edit import DeleteView
#from django.views.generic.base import TemplateView 
from .forms import StudentForm
from django.shortcuts import (get_object_or_404, 
                              render, 
                              HttpResponseRedirect) 


#class CreateStudent( CreateView):
#    model = Student
#    #fields = ['name', 'email', 'password'] #field to be in form
#   form_class = StudentForm  #formclass is used when modelforms are created
# get def() function is used as a get request 

#class ListStudent(ListView):
#    model = Student             #We could explicitly tell the view which template to use by adding a template_name attribute to the view, but in the absence of an explicit template Django will infer one from the object’s name. In this case, the inferred template will be "app/modelname_list.html"
                                  #sucess_url=''  here we can define the url after the extecution of code
                                  #context_data used to specify the name for the data object that we get in template

#class DetailStudent(DetailView):
#    model = Student     

#class UpdateStudent(UpdateView):
#    model = Student
    #fields=['name', 'email', 'password']
#    form_class=StudentForm

#class DeleteStudent(DeleteView):
#    model = Student
    #success_url =




def Create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)     #form returns data to database in python dictionary 
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            reg = Student(name=name, password=password, email=email)
            reg.save()
    else:
        form = StudentForm() 
    return render(request, 'basics/student_form.html', {'form' : form })

def List( request):
    Students= Student.objects.all()
    return render(request, 'basics/student_list.html',{'Students' : Students})

def Detail(request , id):
    stud=Student.objects.get(id= id)
    return render(request, 'basics/student_detail.html',{'stud' : stud})

def Update(request , id):
    if request.method == "POST":
        #obj = get_object_or_404(Student, id = id) 
        pi= Student.objects.get(id= id)
        stud = StudentForm(request.POST, instance=pi) #get data from form and store in stud dict object
        if stud.is_valid():
            stud.save()
            
    
    else:
        pi= Student.objects.get(id= id)
        stud= StudentForm(instance= pi)
    return render(request, 'basics/student_update.html', {'form': stud})

def Delete(request, id):

     obj = get_object_or_404(Student, id = id)  #if exists get object from db else throw 404: not found
     if request.method == "POST":
         
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return HttpResponseRedirect("/")
     
  
     return render(request, "basics/student_confirm_delete.html", {'student': obj })




     #when action is succed the we specify sucess_url= templateview url wich redirect it to templateview in views.py
     #class thanksTemplatleview(TemplateView):
        #template_name= app/thanks.html