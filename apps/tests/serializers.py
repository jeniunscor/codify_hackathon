from rest_framework import serializers

from apps.tests.models import (
    Question,
    Answer,
    Test,
    Course,
    FormForUser, 
    TestResult, 
    OfflineRegistration
)


class OfflineRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfflineRegistration
        fields = (
            'id',
            'user',
            'test', 
            'address', 
            'datetime_selection',
            'date_created',
            'is_approved',
        )


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'text',
        )


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'id',
            'answer',

        )


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = (
            'id',
            'name',
            'form_for_user',
            'course',
            'question',
            'is_demo',
            'level',
        )


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = (
            'id',
            'user', 
            'test', 
            'correct_answers',
            'total_questions',
            'date_completed',
        )
