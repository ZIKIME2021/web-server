from django.contrib import admin
from django.urls import path, include
from . import views

manage_patterns = [
    path('', views.manage, name='manage'),
    path('detail/', views.detail, name='detail'),
    path('detail/add_guest/', views.add_guest, name='add_guest'),
    path('<int:pk>/delete/', views.delete_device, name='delete_device'),
    path('regist_device/', views.regist_device, name='regist_device'),
    path('change-nickname/', views.change_nickname, name='change_nickname')
]

urlpatterns = [
    path('', views.index, name='index'),
    path('lookfor/', views.lookfor, name='lookfor'),
    path('search/', views.search, name='search'),
    path('manage/', include(manage_patterns)),
    path('mypage/<int:pk>/', views.mypage, name='mypage'),
    path('signup/', views.signup, name='signup'),
    path('detail_area/', views.detail_area, name='detail_area'),
    path('login/',views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('sos/', views.sos_request, name='sos_request'),
    path('detail/delete_guest/<int:fk>', views.delete_guest, name='delete_guest'),
]

