from django.urls import path
from .views import index, other_page, RBLoginView, profile, RBLogoutView, ChangeUserInfoView, CreateNewUserView

app_name = 'reclbase'

urlpatterns = [
    path('accounts/register/', CreateNewUserView.as_view(), name='create_user'),
    path('accounts/logout/', RBLogoutView.as_view(), name='logout'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='change_profile'),
    path('accounts/profile/', profile, name='profile'), 
    path('accounts/login/', RBLoginView.as_view(), name='login'),
    path('', index, name='index'),
    path('<str:page>/', other_page, name='other')
]
