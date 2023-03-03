from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    headline = models.CharField(max_length=80)
    sub_headline = models.CharField(max_length=200, null=True)
    repo_link = models.CharField(max_length=150, null=True, default='#')
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="placeholder.png")
    body = RichTextUploadingField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):
        if self.slug is None:
            slug = slugify(self.headline)
            # To make sure slug is unique
            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()
            
            self.slug = slug
        
        super().save(*args, **kwargs)