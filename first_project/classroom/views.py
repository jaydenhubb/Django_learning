from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView,CreateView
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

class ContactFormView(FormView):
    form_class= ContactForm
    template_name = "classroom/contact.html"

    # After successful Validation, Go here=>
    success_url = reverse_lazy('thank_you')
    
    # What to do with a posted valid form
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form) #essentially does this ContactForm(request.POST)