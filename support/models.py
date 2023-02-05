from django.db import models


class FeedbackType(models.Model):
    name = models.CharField('Вид обращения', max_length=50, unique=True)

    class Meta:
        verbose_name = "Вид обращения"
        verbose_name_plural = "Виды обращений"

    def __str__(self):
        return self.name


class Feedback(models.Model):
    feedback_type = models.ForeignKey(FeedbackType, on_delete=models.CASCADE, verbose_name='Тип обращения', related_name='feedbacks')
    subject = models.CharField('Тема обращения', max_length=50)
    content = models.TextField('Описание')
    file = models.FileField('Файл', blank=True)

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"

    def __str__(self):
        return self.subject