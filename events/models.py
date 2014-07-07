from django.db import models

class Item(models.Model):
    IMPORTANCE_CHOICES = (
        ('loc', 'Local'),
        ('nat', 'National'),
        ('for', 'Foreign'),
        )
    title = models.CharField(max_length=255)
    text = models.TextField()
    resources = models.TextField()
    importance = models.CharField(max_length=3, choices=IMPORTANCE_CHOICES, default='nat')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class Event(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)


class People(models.Model):
    birth_date = models.DateTimeField()
    death_date = models.DateTimeField(blank=True, null=True)
