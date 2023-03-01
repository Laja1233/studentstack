from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('register', views.handlelogin, name='handlelogin'),
    path('signup', views.handlesignup, name='handlesignup'),
    path('terms', views.terms, name='terms'),
    path('index2', views.index2, name='index2'),
    path('biology_', views.biology_, name='biology_'),
    path('chemistry_', views.chemistry_, name='chemistry_'),
    path('mathematics_', views.mathematics_, name='mathematics_'),
    path('library_', views.library_, name='library_'),
    path('computerscience_', views.computerscience_, name='computerscience_'),
    path('others', views.others, name='others'),
    path('english_', views.english_, name='english_'),
    path('logout', views.handlelogout, name='logout'),
    path('CC', views.CC, name='CC'),
    path('physics', views.physics, name='physics'),
    path('b_course', views.b_course, name='b_course'),
    path('ch_course', views.ch_course, name='ch_course'),
    path('csc_course', views.csc_course, name='csc_course'),
    path('en_course', views.en_course, name='en_course'),
    path('li_course', views.li_course, name='li_course'),
    path('terms_signup', views.terms_signup, name='terms_signup'),
    path('math_course', views.math_course, name='math_course'),
    path('other_', views.other_, name='other_'),

    path('password-reset/',
     auth_views.PasswordResetView.as_view(template_name='password-reset.html'), 
     name='password-reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), 
     name='password_reset_confirm'),
    
    path('password-reset/done/',
     auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
     name='password_reset_done'),





    
]