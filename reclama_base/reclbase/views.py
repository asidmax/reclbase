from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import ReclUser
from .forms import ChangeUserInfoForm, UserRegistrationForm


def index(request):
    return render(request, 'recl/index.html')


def other_page(request, page):
    try:
        template = get_template('recl/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


class RBLoginView(LoginView):
    template_name = 'recl/login.html'


@login_required
def profile(request):
    return render(request, 'recl/profile.html')


class RBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'recl/logout.html'


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = ReclUser
    template_name = 'recl/change_profile.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('recl:profile')
    success_message = 'Информация успешно изменена'

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class CreateNewUserView(CreateView):
    model = ReclUser
    template_name = 'recl/create_user.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('reclbase:index')
