from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project, ExpertReview

# Create your views here.

class IndexView(ListView):
    model = Project
    template_name = 'index.html'


class ProjectView(DetailView):
    queryset = Project.objects.all()
    context_object_name = 'project'
    template_name = 'project.html'

class ReviewDetialView(DetailView):
    queryset = ExpertReview.objects.all()
    context_object_name = 'review'
    template_name = 'review.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['project_list'] = Project.objects.filter(review=self.object)
        return context


