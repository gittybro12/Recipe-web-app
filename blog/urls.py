from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.postViews.as_view(), name='Home'),
    path('post/<int:pk>', views.detailed_view.as_view(), name='post'),
    path('post_create/', views.create_view.as_view(), name='post-create'),
    path('post_update/<int:pk>', views.update_view.as_view(), name='post-update'),
    path('post_delete/<int:pk>', views.delete_view.as_view(), name='post-delete'),
    path('search_result/',views.search, name='search-result'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)