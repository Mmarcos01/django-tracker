from django.urls import path
from .views import TrackerListView, TrackerDetailView, TrackerCreateView, TrackerUpdateView, TrackerDeleteView 

urlpatterns = [
    path('', TrackerListView.as_view(), name="track_list"),
    path('create/', TrackerCreateView.as_view(), name="track_create"),
    path('<int:pk>/', TrackerDetailView.as_view(), name="track_detail"),
    path('<int:pk>/update/', TrackerUpdateView.as_view(), name="track_update"),
    path('<int:pk>/delete/', TrackerDeleteView.as_view(), name="track_delete"),
] 

