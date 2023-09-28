from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("register/", views.register, name="register"),
  path("login/", views.loginView, name="login"),
  path("logout", views.logoutRequest, name= "logout"),
  path("blog/create", views.createBlog, name="createBlog"),
  path("blog/show", views.showBlogs, name="showBlogs"),
  path("blog/myBlogs", views.myBlogs, name="myBlogs"),
  path("blog/id/<int:id>/", views.blogPage, name="blogPage"),
  path("blog/AddComment/blog_id/<int:blog_id>/", views.addComment, name="addComment"),
  path("blog/edit/id/<int:blog_id>", views.editBlog, name="editBlog"),
  path("blog/delete/id/<int:blog_id>", views.deleteBlog, name="deleteBlog"),
  path("comment/delete/id/<int:id>/<int:blog_id>", views.deleteComment, name="deleteComment"),
]