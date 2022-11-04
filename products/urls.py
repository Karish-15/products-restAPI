from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('', views.ProductListCreateView.as_view()),
    path('<int:pk>/delete', views.ProductDeleteView.as_view()),
    path('<int:pk>/update', views.ProductUpdateView.as_view()),
]
