from django.db import models
from django.utils import timezone

# Create your models here.


class File(models.Model):
    region = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    community = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    family_name = models.CharField(max_length=200)
    intervention_sector = models.CharField(max_length=200)
    reluctant_houses = models.NullBooleanField(blank=True, null=True, default=None,)
    members = models.IntegerField()
    registration_date = models.DateField()
    sex = models.CharField(max_length=2)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.family_name


class Statement(models.Model):
    file = models.ForeignKey(
        'File',
        on_delete=models.CASCADE,
    )
    title = models.TextField(max_length=200)
    order = models.IntegerField()
    answer_value = models.CharField(
        max_length=2)

    def __str__(self):
        return self.title


class StatementTest(models.Model):
    title = models.TextField(max_length=200)
    order = models.IntegerField()
    answer_value = models.CharField(
        max_length=2, null=True, blank=True)

    def __str__(self):
        return self.title
