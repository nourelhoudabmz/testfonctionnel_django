from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from userapp import views

urlpatterns = [
                  path('signup/', views.signup, name='signup'),

                  # -----------------------Category urls------------
                  path('', views.GetCategory.as_view(), name='all-categories'),
                  path('allcategory/', views.GetCategory.as_view(), name='all-categories'),
                  path('create-category/', views.CreateCategory.as_view()),
                  path('update-category/<int:pk>', views.UpdateCategory.as_view()),
                  path('delete-category/<int:pk>', views.DeleteCategory.as_view()),

                  # -----------------------Tags urls--------------------
                  path('create-tag/', views.CreateTag.as_view()),
                  path('all-tags/', views.GetTag.as_view(), name='all-tags'),
                  path('update-tag/<int:pk>', views.UpdateTag.as_view()),
                  path('delete-tag/<int:pk>', views.DeleteTag.as_view()),

                  # -----------------------Product urls--------------------
                  path('all-product/', views.GetProduct.as_view(), name='all-product'),
                  path('create-product/', views.CreateProduct.as_view()),
                  path('update-product/<int:pk>', views.UpdateProduct.as_view()),
                  path('delete-product/<int:pk>', views.DeleteProduct.as_view()),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
