from django.shortcuts import render
from .models import Track
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


class TrackerListView(ListView):
    template_name = 'track-list.html'
    model = Track
    context_object_name = 'list_tracker'

class TrackerDetailView(DetailView):
    template_name = 'track-detail.html'
    model = Track

class TrackerCreateView(CreateView):
    template_name = 'track-create.html'
    model = Track
    fields = ['title', 'description', 'purchaser']
    success_url = reverse_lazy('track_list')

class TrackerUpdateView(UpdateView):
    template_name = 'track-update.html'
    model = Track
    fields = ['title', 'description', 'purchaser']

class TrackerDeleteView(DeleteView):
    template_name = 'track-delete.html'
    model = Track
    success_url = reverse_lazy('track_list')
