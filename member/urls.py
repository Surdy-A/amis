from django.urls import path
from .views import (SchoolListView, SchoolDetailView, workshop_view, exam_view, delegate_view, calender_reg_view,
                    PrimaryCompetitionListView, JssCompetitionListView, SssCompetitionListView, PrimaryCompetitionDetailView, primary_competition_reg_view,
                    jss_competition_reg_view, sss_competition_reg_view, WorkshopListView, ExamListView, CalenderListView)

app_name = 'member'

urlpatterns = [
    path('schools', SchoolListView.as_view(), name='schools'),
    path('school/<slug:slug>/', SchoolDetailView.as_view(), name='school_detail'),
    path('workshop', workshop_view, name='workshop'),
    path('delegate', delegate_view, name='delegate'),
    path('calender', calender_reg_view, name='calender'),
    path('competition/primary/', PrimaryCompetitionListView.as_view(), name='primary_competition'),
    path('competition/jss/', JssCompetitionListView.as_view(), name='jss_competition'),
    path('competition/sss/', SssCompetitionListView.as_view(), name='sss_competition'),
    path('school/<slug:slug>/', PrimaryCompetitionDetailView.as_view(), name='competition_detail'),
    path('competition/primary/add', primary_competition_reg_view, name='add_primary_competition'),
    path('competition/jss/add', jss_competition_reg_view, name='add_jss_competition'),
    path('competition/sss/add', sss_competition_reg_view, name='add_sss_competition'),
    path('workshop/view/', WorkshopListView.as_view(), name='workshop_view'),
    path('calender/view/', CalenderListView.as_view(), name='calender_view'),
    path('exam', exam_view, name='exam'),
    path('exam/view/', ExamListView.as_view(), name='exam_view')
]
