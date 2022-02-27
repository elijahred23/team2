from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [ path("veterans/", views.VeteranList.as_view()),
                path("veterans/<int:pk>/", views.VeteranDetail.as_view()),
                path("interview/", views.InterviewList.as_view()),
                path("interview/<int:pk>/", views.InterviewDetail.as_view()),
                ]

urlpatterns = format_suffix_patterns(urlpatterns)

"""path("veterans/", views.VeteranList.as_view()),
    path("veterans/<int:pk>", views.VeteranDetail.as_view()),
    path("veterans/", views.VeteranList.as_view()),
    path("veterans/<int:pk>", views.VeteranDetail.as_view()),"""