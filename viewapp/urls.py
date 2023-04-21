from django.urls import path
from django.views.generic import TemplateView
from .views import WatchView, ContactView, CreateWatchView, WatchDetail, DeleteWatchView, UpdateWatchView

urlpatterns = [
    path('', WatchView.as_view(), name="home_page_view"),
    path('admin-panel/', TemplateView.as_view(template_name = "pages/admin.html"), name="admin_page"),
    path('product/', WatchView.as_view(template_name="pages/product.html"), name="product_page_view"),
    path('contact/', ContactView.as_view(), name="contact_page_view"),
    path('watch/<int:pk>/', WatchDetail.as_view(), name="watch_detail"),
    path('bought/', WatchView.as_view(template_name="pages/services.html"), name="bought_page_view"),
    path('create/', CreateWatchView.as_view(), name="create_watch"),
    path('delete/<int:pk>/', DeleteWatchView.as_view(), name="delete_watch"),
    path('update/<int:pk>/', UpdateWatchView.as_view(), name="update_watch")
]