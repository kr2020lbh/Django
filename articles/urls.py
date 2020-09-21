from django.urls import path,include
from . import views
app_name = 'articles'
urlpatterns = [
    path('', views.index,name='index'),
    path('create/',views.create,name='create'),
    path('detail/<int:article_pk>',views.detail,name='detail'),
    path('update/<int:article_pk>',views.update,name='update'),
    path('delete/<int:article_pk>',views.delete,name='delete'),
    path('comment_create/<int:article_pk>',views.comment_create,name='comment_create'),
    path('comment_delete/<int:article_pk>/<int:comment_pk>',views.comment_delete,name='comment_delete'),
]
