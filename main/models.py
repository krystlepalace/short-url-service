import random
from django.conf import settings
from django.db import models


class Tokens(models.Model):
    '''Модель таблицы для хранения токенов'''
    full_link = models.URLField(unique=True)
    short_link = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        while True:
            self.short_link = ''.join(random.choices(settings.ALPHABET, k=settings.LENGTH))
            if not Tokens.objects.filter(short_link=self.short_link).exists():
                break
        super().save(*args, **kwargs)
