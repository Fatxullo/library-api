from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookListCreateApiView, BookUpdateDeleteApiView, BookViewSet


router = SimpleRouter()
router.register('books', BookViewSet, basename='books')


urlpatterns = [
    # path('booklistcreate/', BookListCreateApiView.as_view()),
    # path('bookupdatedelete/<int:pk>/', BookUpdateDeleteApiView.as_view()),   
]

urlpatterns = urlpatterns + router.urls