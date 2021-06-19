from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview,name="home"),
    path('signup',views.signupview,name="signup"),
    path('login',views.loginview,name="login"),
    path('logout',views.logoutview,name="logout"),
    path('add_blog',views.add_blogview,name="add_blog"),
    path('save_blog',views.save_postview,name="save_blog"),
    path('show_post',views.show_postview,name="show_post"),
    path('posts/<slug:posturl>',views.post_detailview,name='post_detail'),
    path('edit/<slug:posturl>',views.edit_postview,name='edit_post'),
    path('update/<slug:posturl>',views.update_postview,name='update_post'),
    path('delete/<slug:posturl>',views.delete_view,name='delete_post'),
    path('category/<type>',views.category_view,name='category'),
    path('about',views.aboutview,name="about")
]
