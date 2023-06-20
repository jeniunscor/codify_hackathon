from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apps.tests.models import (
    Test, Question, Answer, TestResult, OfflineRegistration
)
from apps.tests.serializers import (
    TestSerializer, TestResultSerializer,
    OfflineRegistrationSerializer
)


class OfflineRegistrationCreateView(generics.CreateAPIView):
    queryset = OfflineRegistration.objects.all()
    serializer_class = OfflineRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestListView(APIView):
    def get(self, request):
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)


class TestSubmissionView(APIView):
    def post(self, request):
        test_id = request.data.get('test_id')
        user_answers = request.data.get('answers')

        test = get_object_or_404(Test, id=test_id)

        correct_answers = 0
        total_questions = test.question.count()

        for answer in user_answers:
            try:
                question = Question.objects.get(id=answer['question_id'])
                selected_answer = Answer.objects.get(id=answer['answer_id'])
            except (Question.DoesNotExist, Answer.DoesNotExist):
                return Response({"error": "Invalid question or answer"}, status=404)

            if selected_answer.is_true and selected_answer.question == question:
                correct_answers += 1

        result = TestResult.objects.create(
            user=request.user, test=test,
            correct_answers=correct_answers, total_questions=total_questions
        )
        serializer = TestResultSerializer(result)
        return Response(serializer.data, status=201)


class TestResultView(APIView):
    def get(self, request):
        results = TestResult.objects.filter(user=request.user)
        serializer = TestResultSerializer(results, many=True)
        return Response(serializer.data)


class QuizDetailView(APIView):
    def get(self, request, test_id):
        test = get_object_or_404(Test, id=test_id)

        is_completed = TestResult.objects.filter(user=request.user, test=test).exists()

        correct_answers = {}
        for question in test.question.all():
            answers = Answer.objects.filter(question=question, is_true=True)
            correct_answers[question.id] = [answer.id for answer in answers]

        serializer = TestSerializer(test, context={'is_completed': is_completed, 'correct_answers': correct_answers})
        return Response(serializer.data)
