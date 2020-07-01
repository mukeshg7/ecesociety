from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('faculty/', views.FacultyList.as_view()),
    path('faculty/<int:pk>/', views.FacultyDetail.as_view()),
    path('notice/',views.NoticeList.as_view()),
    path('notice/<int:pk>/', views.NoticeDetail.as_view()),
    path('member/',views.MemberList.as_view()),
    path('member/<int:pk>',views.MemberDetail.as_view()),
]