from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/',views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('logout/',views.logout, name='logout'),
    path('profile/<str:pk>',views.profile, name='profile'),
    path('settings',views.settings, name='settings'),
    path('upload/',views.upload, name='upload'),
    path('like/',views.like, name='like'),
    path('follow/',views.follow, name='follow'),
    path('search',views.search, name='search'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),

]
