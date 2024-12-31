
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.middleware.csrf import get_token
from django.http import JsonResponse, HttpResponse

def csrf(request):
    response = JsonResponse({"csrfToken": get_token(request)})
    response["Access-Control-Allow-Origin"] = "http://localhost:5173"
    response["Access-Control-Allow-Credentials"] = "true"
    response.set_cookie("csrftoken", get_token(request))
    return response

def home_view(request):
    return HttpResponse("Hello from Django root path!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('accounts/', include('allauth.urls')), 
    path("accounts/csrf/", csrf),
    path('', home_view, name='home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
