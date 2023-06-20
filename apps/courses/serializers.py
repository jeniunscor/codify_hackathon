from rest_framework import serializers

from apps.courses.models import Category, Course, Faq, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'photo',
        )


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = (
            'id',
            'name',
            'category',
        )


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'title',
            'subtitle',
            'category',
            'description',
            'photo',
        )


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = (
            'question',
            'answer',
        )
