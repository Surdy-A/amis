# Create your models here.
from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.text import slugify
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(blank=True, default='')
    created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="img")
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(1920, 1281)],
                                     format='JPEG',
                                     options={'quality': 95})
    slug = models.SlugField(max_length=200, db_index=True, default='')

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
       value = self.title
       self.slug = slugify(value, allow_unicode=True)
       super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args={self.slug})
        