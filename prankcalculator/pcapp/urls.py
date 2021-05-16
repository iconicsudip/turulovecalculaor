from . import views
from django.urls import path
urlpatterns = [
    path('',views.signup,name="signup"),
    path('signup/',views.signup,name="signup"),
    path('dashboard/<str:uname>',views.dashboard,name="dashboard"),
    path('dashboard/',views.signup,name="dashboard/"),
    path('submitted/<str:url>',views.submitted,name="submitted"),
    path('logout/',views.logout,name="logout"),
    path('signin/',views.signin,name="signin"),
    path('thankyou/<str:url>',views.thankyou,name="thankyou"),
    path('<str:link>/',views.main_view,name='main_view'),
]