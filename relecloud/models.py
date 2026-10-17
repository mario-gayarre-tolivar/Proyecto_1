from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Destination(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
        )
    description = models.TextField(
        null=True,
        blank=True,
        max_length=2000
        )
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('destination_detail', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.name

        

class Cruise(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
        )
    description = models.TextField(
        null=True,
        blank=True,
        max_length=2000
        )
    destinations = models.ManyToManyField(
        'Destination',
         related_name='cruises'
        )

    def __str__(self) -> str:
        return self.name


class InfoRequest(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    email = models.EmailField()
    cruise = models.ForeignKey(
        'Cruise',
        on_delete=models.CASCADE,
    )
    notes = models.TextField(
        max_length=2000,
        null=False,
        blank=False,
    )

    def __str__(self) -> str:
        return self.name