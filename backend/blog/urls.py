from blog.views import BlogpostCategoryView,BlogpostDetailView,BlogpostFeaturedView,BlogpostListView
from django.urls import path

urlpatterns = [
    path('',BlogpostListView.as_view()),
    path('<slug>',BlogpostDetailView.as_view()),
    path('category',BlogpostCategoryView.as_view()),
    path('featured',BlogpostFeaturedView.as_view()),
]