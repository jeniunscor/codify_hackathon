from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название", unique=True
    )
    photo = models.FileField(upload_to='category/')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название", unique=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория",
        related_name="sub_categories"
    )
    photo = models.FileField(upload_to='category/')

    class Meta:
        verbose_name = 'ПодКатегория'
        verbose_name_plural = 'ПодКатегории'

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.FileField(upload_to='photos/', verbose_name="Картина")

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.image.name


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    subtitle = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Подзаголовок"
    )
    category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, verbose_name="Категория",
        related_name="Courses"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name='Описание теста'
    )
    photo = models.ForeignKey(
        Photo, on_delete=models.CASCADE, verbose_name="Картина",
        related_name="Courses"
    )
    topic = models.TextField(
        verbose_name='Тема'
    )

    class Meta:
        verbose_name = 'Cпециальность'
        verbose_name_plural = 'Cпециальности'

    def __str__(self):
        return self.title


class Faq(models.Model):
    question = models.CharField(
        max_length=200, verbose_name='Вопрос'
    )
    answer = models.TextField(verbose_name='Ответ')

    class Meta:
        verbose_name = 'Часто Задаваемый Вопрос'
        verbose_name_plural = 'Часто Задаваемые Вопросы'

    def __str__(self):
        return f'{self.question} - {self.answer}'
