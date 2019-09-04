from django.db import models
from django.utils import timezone

# Create your models here.

# class Person(models.Model):
#     # first_name = models.CharField(max_length=20)
#     # last_name = models.CharField(max_length=20)
#     # email = models.EmailField(max_length=250)
#     # phone = models.CharField(max_length=50)
#     category = models.CharField(max_length=20)
#     label = models.CharField(max_length=20)
#     link = models.CharField(max_length=200)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     # def full_name(self):
#     #     return '{} {}'.format(self.first_name, self.last_name)
#
#     # def __str__(self):
#     #     return self.full_name()


class Link(models.Model):

    category = models.CharField(max_length=20)
    label = models.CharField(max_length=20)
    link = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
