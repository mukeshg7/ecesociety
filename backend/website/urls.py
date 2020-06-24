from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from website import views

urlpatterns=[
				path('faculty/',views.FacultyList.as_view(), name='faculty-list'),
				path('members/',views.MemberList.as_view(),name='members-list'),
				path('notice/',views.NoticeList.as_view(),name='notice-list'),
				path('api/',views.api_root),
			]

