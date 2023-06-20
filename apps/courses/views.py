from rest_framework import generics

from apps.courses.serializers import (
    CategorySerializer,
    CourseSerializer,
    FaqSerializer,
    SubCategorySerializer
)
from apps.courses.models import (
    Category,
    Course,
    Faq,
    SubCategory
)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryDetailView(generics.RetrieveAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()


class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class FAQListView(generics.ListAPIView):
    serializer_class = FaqSerializer
    queryset = Faq.objects.all()
