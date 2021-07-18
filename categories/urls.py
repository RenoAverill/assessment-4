from django.urls import path
from . import views


urlpatterns = [
    # category paths
    path('', views.category_list, name='category_list'),
    path("new", views.category_new, name='category_new'),
    path("<int:category_id>", views.category_detail, name='category_detail'),
    path("<int:category_id>/edit", views.category_edit, name='category_edit'),
    path("<int:category_id>/delete", views.category_delete, name='category_delete'),

    # post paths
    path('<int:category_id>/posts', views.post_list, name='post_list'),
    path("<int:category_id>/posts/new", views.post_new, name='post_new'),
    path("<int:category_id>/posts/<int:post_id>",
         views.post_detail, name='post_detail'),
    path("<int:category_id>/posts/<int:post_id>/edit",
         views.post_edit, name='post_edit'),
    path("<int:category_id>/posts/<int:post_id>/delete",
         views.post_delete, name='post_delete'),
]
