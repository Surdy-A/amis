from django.views.generic import ListView, DetailView
from member.models import School, PrimaryCompetition, JSSCompetition, SSSCompetition, Workshop, CalenderRegistration, Exam
from .forms import WorkshopForm, DelegateForm, CalenderRegForm, PrimaryCompetitionRegForm, JSSCompetitionRegForm, SSSCompetitionRegForm, ExamForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render

class SchoolListView(ListView):
    model = School
    template_name = 'school/school_list.html'
    context_object_name = 'school_list'
    paginate_by = 100


class SchoolDetailView(DetailView):
    model = School
    template_name = 'school/school_detail.html'
    context_object_name = 'school_detail'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['latest_shools'] = School.objects.all()
        return context


def workshop_view(request):
    context = {}
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
     # create object of form
        form = WorkshopForm(request.POST or None, request.FILES or None)
        # check if form data is valid
        if form.is_valid():
            print("value ", form.cleaned_data['workshop_name'])
        # save the form data to model
            form.save()
            messages.success(request, 'Form submission successful')

            return HttpResponseRedirect('/')

    else:
        form = WorkshopForm()
    context['form'] = form
    return render(request, "school/workshop.html", context)

def delegate_view(request):
    context = {}
    if request.method == 'POST':
        form = DelegateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print("value ", form.cleaned_data['workshop_name'])
            form.save()
            messages.success(request, 'Delegate added successfully')
            return HttpResponseRedirect('/member/workshop')
    else:
        form = DelegateForm()
    context['form'] = form
    return render(request, "school/delegate.html", context)


def calender_reg_view(request):
    context = {}
    if request.method == 'POST':
        form = CalenderRegForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully register for calender printing')
            return HttpResponseRedirect('/')
    else:
        form = CalenderRegForm()
    context['form'] = form
    return render(request, "school/calender_reg.html", context)


class PrimaryCompetitionListView(ListView):
    model = PrimaryCompetition
    template_name = 'school/primary_competition.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['primary_competition_list'] = PrimaryCompetition.objects.all()
        return context

class JssCompetitionListView(ListView):
    model =JSSCompetition
    template_name = 'school/jss_competition.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jss_competition_list'] = JSSCompetition.objects.all()
        return context

class SssCompetitionListView(ListView):
    model =SSSCompetition
    template_name = 'school/sss_competition.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sss_competition_list'] = SSSCompetition.objects.all()
        return context


class WorkshopListView(ListView):
    model = Workshop
    template_name = 'school/workshop_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workshop_list'] = Workshop.objects.all()
        return context

class CalenderListView(ListView):
    model = Workshop
    template_name = 'school/calender_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['calender_list'] = CalenderRegistration.objects.all()
        return context

class PrimaryCompetitionDetailView(DetailView):
    model = PrimaryCompetition
    template_name = 'school/primary_competition.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_competition'] = PrimaryCompetition.objects.all()


def primary_competition_reg_view(request):
    context = {}
    if request.method == 'POST':
        form = PrimaryCompetitionRegForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully register for primary category competition')
            return HttpResponseRedirect('/')
    else:
        form = PrimaryCompetitionRegForm()
    context['form'] = form
    return render(request, "school/add_primary_competition.html", context)

def jss_competition_reg_view(request):
    context = {}
    if request.method == 'POST':
        form = JSSCompetitionRegForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully register for jss category competition')
            return HttpResponseRedirect('/')
    else:
        form = JSSCompetitionRegForm()
    context['form'] = form
    return render(request, "school/add_jss_competition.html", context)

def sss_competition_reg_view(request):
    context = {}
    if request.method == 'POST':
        form = SSSCompetitionRegForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully register for sss category competition')
            return HttpResponseRedirect('/')
    else:
        form = SSSCompetitionRegForm()
    context['form'] = form
    return render(request, "school/add_sss_competition.html", context)

#ExamForm View
def exam_view(request):
    context = {}
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
     # create object of form
        form = ExamForm(request.POST or None, request.FILES or None)
        # check if form data is valid
        if form.is_valid():
        # save the form data to model
            form.save()
            messages.success(request, 'Form submission successful')

            return HttpResponseRedirect('/')

    else:
        form = ExamForm()
    context['form'] = form
    return render(request, "school/examform.html", context)


class ExamListView(ListView):
    model = Exam
    template_name = 'school/exam_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam_list'] = Exam.objects.all()
        return context