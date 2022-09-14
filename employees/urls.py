from django.urls import path
from django.conf import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path(r'', ViewList.as_view()),
    path(r'<int:id>/', ViewList.get_detail),
    path(r'sort/', ViewList.sort),
    path(r'searches_list/', ViewList.search_list),
    # path(r'update_employee', V)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)