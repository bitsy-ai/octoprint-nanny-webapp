import logging
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.apps import apps
from django.views.generic import TemplateView, DetailView, FormView
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from rest_framework.authtoken.models import Token
from .forms import TimelapseUploadForm
from print_nanny_webapp.alerts.tasks import analyze_timelapse_video

User = get_user_model()
TimelapseAlert = apps.get_model('alerts', 'TimelapseAlert')

logger = logging.getLogger(__name__)


class DashboardView(LoginRequiredMixin, TemplateView):
    pass

ecommerce_dashboard_view = DashboardView.as_view(template_name="dashboard/ecommerce.html")
crm_dashboard_view = DashboardView.as_view(template_name="dashboard/crm.html")
analytics_dashboard_view = DashboardView.as_view(template_name="dashboard/analytics.html")
projects_dashboard_view = DashboardView.as_view(template_name="dashboard/projects.html")


class HomeDashboardView(LoginRequiredMixin, DetailView, FormView):

    model = User
    template_name = 'dashboard/home.html'
    success_url = 'videos/'

    form_class = TimelapseUploadForm

    def form_valid(self, form):

        timelapse_alert = TimelapseAlert.objects.create(
            user=self.request.user,
            original_video=self.request.FILES['video_file'],
        )

        video_file = self.request.FILES['video_file']

        if isinstance(video_file, InMemoryUploadedFile):
            logging.info(f'File processed asInMemoryUploadedFile')
            logging.info(f'File info {timelapse_alert.original_video}')
            analyze_timelapse_video.delay(
                timelapse_alert.id, 
                timelapse_alert.original_video.url
            )
        elif isinstance(video_file, TemporaryUploadedFile):
            logging.info(f'File processed as TemporaryUploadedFile')
            analyze_timelapse_video.delay(
                timelapse_alert.id, 
                self.request.FILES['video_file'].temporary_file_path()
            )
        return super().form_valid(form)

    def get_object(self):
        token, created = Token.objects.get_or_create(user=self.request.user)
        self.request.user.token = token
        self.request.user.active_alerts = self.request.user.alertmessage_set.filter(seen=False)
        return self.request.user
    
    # def get_context_data(self, **kwargs):
    #     context = super(HomeDashboardView, self).get_context_data(**kwargs)
    #     context['timelapse_form'] = TimelapseUploadForm()
    #     return context

home_dashboard_view = HomeDashboardView.as_view()


class DemoDashboardView(LoginRequiredMixin, DetailView):

    model = User
    template_name = 'dashboard/demo.html'
    def get_object(self):
        token, created = Token.objects.get_or_create(user=self.request.user)
        self.request.user.token = token
        self.request.user.active_alerts = self.request.user.alertmessage_set.filter(last_action=AlertMessage.ActionChoices.PENDING)
        return self.request.user

demo_dashboard_view = DemoDashboardView.as_view()


class VideoDashboardView(LoginRequiredMixin, DetailView):

    model = User
    template_name = 'dashboard/video.html'
    def get_object(self):
        token, created = Token.objects.get_or_create(user=self.request.user)
        self.request.user.token = token
        self.request.user.active_alerts = self.request.user.alertmessage_set.filter(last_action=AlertMessage.ActionChoices.PENDING)
        return self.request.user

video_dashboard_view = VideoDashboardView.as_view()