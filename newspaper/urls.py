from django.urls import path
from newspaper import views

urlpatterns = [
    path(
        "",
        views.HomeView.as_view(),
        name="home"
    ),
    path(
        "post-detail/<int:pk>/",
        views.PostDetailview.as_view(),
        name="post-detail",
    ),
    path(
        "post-list",
        views.PostListView.as_view(),
        name="post-list",
    ),
    path(
        "post-search/",
        views.PostSearchView.as_view(),
        name="post-search",
    ),
    path(
        "newsletter/",
        views.NewsLetterView.as_view(),
        name="newsletter",
    ),
    path(
        "post-by-category/<int:cat_id>/",
        views.PostByCategory.as_view(),
        name="post-by-category",
    ),
    path(
        "post-by-tag/<int:tag_id>/",
        views.PostByTag.as_view(),
        name="post-by-tag",
    ),
    path(
        "about/",views.
         AboutUsView.as_view(),
         name="about-us",
         ),
         
    path(
        "contact/",
         views.ContactView.as_view(),
         name="contact",
         ),


    path(
        "comment/",
         views.CommentView.as_view(),
         name="comment",
         ),
]
