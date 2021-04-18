from django.urls import path
from . import views
from django.conf.urls.static import static
from my_project import settings

app_name = 'boards'
urlpatterns = [
    path('',views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/',views.PostDetailView.as_view(), name='post_detail'),
    path('new/', views.PostLCreateView.as_view(), name ='post_new'),
    path('new/<int:board_pk>', views.PostLCreateView.as_view(), name ='each_new'),
    path('<int:board_pk>/<int:pk>/',views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit',views.PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete',views.PostDeleteView.as_view(), name='post_delete'),
    path('num/<int:board_pk>/',views.PostListView.as_view(), name = 'each_list'),
    path('<int:post_pk>/comments/new', views.CommentCreateView.as_view(), name = "comment_new"),
    path('<int:post_pk>/comments<int:pk>/delete', views.CommentDeleteView.as_view(), name = "comment_delete"),
    path('search_board/',views.BoardListView.as_view(), name = 'search_board'),
    path('board_list/', views.BoardListView.as_view(), name = 'board_list'),
]


