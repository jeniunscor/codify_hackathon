from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.courses.views import (
    CategoryListView,
    CategoryDetailView,
    CourseDetailView,
    CourseListView,
    FAQListView,
    SubCategoryListView,
    SubCategoryDetailView,
 )
from apps.tests import views
from apps.users.views import (
    RegisterView,
    LoginView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="LevelUp",
      default_version='v1',
      description="username:user / password:user",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


api_v1 = [
    path("categories/", CategoryListView.as_view()),
    path("category/<int:pk>", CategoryDetailView.as_view()),
    path("directions/", CourseListView.as_view()),
    path("direction/<int:pk>", CourseDetailView.as_view()),
    path('faq/', FAQListView.as_view()),
    path('subcategory/', SubCategoryListView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('tests/', views.TestListView.as_view(), name='test-list'),
    path('tests/<int:test_id>/', views.QuizDetailView.as_view(), name='quiz-detail'),
    path('tests/submit/', views.TestSubmissionView.as_view(), name='test-submit'),
    path('results/', views.TestResultView.as_view(), name='test-results'),
    path('offline_reg/', views.OfflineRegistrationCreateView.as_view(), name='offline-reg'),

]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_v1)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]
