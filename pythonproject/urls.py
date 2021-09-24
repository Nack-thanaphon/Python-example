from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
from django.conf import settings
from  django.conf.urls.static import static

urlpatterns = [
    path ('index/',views.index),
    path ('addnews/',views.addnews),
    path ('addnewsdata/',views.addnewsdata,name='addnewsdata'),
    path ('contentmanager/',views.contentmanager),
    path ('contentedit/',views.contentedit,name='contentedit'),
    path ('contentupdate',views.contentupdate,name='contentupdate'),
    path ('contentdeleate',views.contentdeleate,name='contentdeleate'),
    path ('contentresult',views.contentresult,name='contentresult'),
    path ('register',views.register),
    path ('registerdata',views.registerdata,name='registerdata'),
    path ('login',views.login),
    path ('logincheck',views.logincheck,name='logincheck'),
    path ('logoff',views.logoff),
    path ('warnning',views.warnning)
    
 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)