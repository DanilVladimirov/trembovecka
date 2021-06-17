from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from siteapp.views import *
from trembovetska import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_page'),
    path('', main_page, name='main_page'),
    path('create_post/', create_post, name='create_post'),
    path('del_post/', del_post, name='del_post'),
    path('contact/', contact_page, name='contact_page'),
    path('register_cons/', register_cons, name='register_cons'),
    path('files/', files_page, name='files_page'),
    path('category/<int:cid>/', category_page, name='category_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('register/', registration_page, name='register_page'),
    path('forum/', forum_page, name='forum_page'),
    path('create-theme/', forum_create_theme, name='create_theme'),
    path('forum-theme/<int:theme_id>/', forum_theme, name='forum_theme'),
    path('news/', news_page, name='news_page'),
    path('group/', about_group, name='group_page')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
