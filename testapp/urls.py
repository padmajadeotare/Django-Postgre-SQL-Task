from testapp import views
from django.urls import path

urlpatterns = [
    # path('apicbv/',views.PersonalDetailCBV.as_view),
    path('inform/', views.InformView.as_view()),
    path('info/', views.InfoView.as_view(), name='create_job'),
]
