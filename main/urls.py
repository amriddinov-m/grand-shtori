from django.urls import path
from django.views.generic import TemplateView

from main.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('.well-known/pki-validation/83579306C8035DE45221B281A5E5D2B7.txt', TemplateView.as_view(
        template_name="83579306C8035DE45221B281A5E5D2B7.txt", content_type="text/plain")),
]
