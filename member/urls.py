from django.urls import path
from .views import (SchoolListView, SchoolDetailView, workshop_view, delegate_view, calender_reg_view, 
                    PrimaryCompetitionListView, PrimaryCompetitionDetailView, primary_competition_reg_view)

app_name = 'member'

urlpatterns = [
    path('schools', SchoolListView.as_view(), name='schools'),
    path('school/<slug:slug>/', SchoolDetailView.as_view(), name='school_detail'),
    path('workshop', workshop_view, name='workshop'),
    path('delegate', delegate_view, name='delegate'),
    path('calender', calender_reg_view, name='calender'),
    path('competition/primary/', PrimaryCompetitionListView.as_view(), name='primary_competition'),
    path('school/<slug:slug>/', PrimaryCompetitionDetailView.as_view(), name='competition_detail'),
    path('competition/primary/add', primary_competition_reg_view, name='add_primary_competition'),
]
