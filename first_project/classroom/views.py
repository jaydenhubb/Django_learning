from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (TemplateView, FormView,
                                  CreateView, ListView,
                                  DetailView, UpdateView)
from classroom.forms import ContactForm
from classroom.models import Teacher

# Create your views here.

class HomeView(TemplateView):
    template_name = "classroom/home.html"

class ThankYouView(TemplateView):
    template_name ="classroom/thank_you.html"


class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy("thank_you")

class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teacher_list'
class ContactFormView(FormView):
    form_class= ContactForm
    template_name = "classroom/contact.html"

    # After successful Validation, Go here=>
    success_url = reverse_lazy('thank_you')
    
    # What to do with a posted valid form
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form) #essentially does this ContactForm(request.POST)
    
class TeacherDetailView(DetailView):
    model = Teacher

class TeacherUpdateView(UpdateView):
    # Going to share the modelform.html template
    model = Teacher
    fields = ['last_name']
    success_url= reverse_lazy("teacher_list")
