from django.db import models


class CreatedAndUpdatedAbstractModel(models.Model):
    """
        Абстрактная модель для хранения полей времени создания и обновления записи
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания задачи')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления задачи')

    class Meta:
        abstract = True
