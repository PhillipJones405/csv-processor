from django.urls import path
from .views import FileUploadView, SignupView, UserInfoView, LoginView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('user-info/', UserInfoView.as_view(), name='user-info'),
    path('login/', LoginView.as_view(), name='login'),
]
