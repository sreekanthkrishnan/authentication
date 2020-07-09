from django.conf.urls import url
from web import views
app_name = 'web'
urlpatterns = [
    url(r'signup',views.signup,name='signup'),
    url(r'login',views.login_form,name='login')
]