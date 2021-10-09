from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import index, rew, second_index

urlpatterns = [
    path('', index, name='index'),
    path('rew/<int:id>', rew, name='rew'),
    path('reference/<number_of_passport>', second_index, name='reference')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
