from django.conf.urls import url
from mapp import views

app_name = 'mapp'

urlpatterns = [
    url(r'^register/$', views.reg , name='regit'),
    url(r'^login/$', views.lgn, name='logit'),
]
# { % if user.is_authenticated %}
# < li > < a
# href = "{url 'logout'}"
# class ="navbar-link" > Login < / a > < / li >
# { % else %}
# < li > < a
# href = "{% url 'mapp:user_login' %}"
#
#
# class ="navbar-link" > logout < / a > < / li >
#
#
# { % endif %}
