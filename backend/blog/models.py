from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

# Create your models here.
class Categories(models.TextChoices):
    CHOICE1 = 'choice1'
    CHOICE2 = 'choice2'
    CHOICE3 = 'choice3'
    CHOICE4 = 'choice4'

class Blogpost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(max_length=50,choices=Categories.choices,default= Categories.CHOICE1)
    excerpt = models.CharField(max_length=150)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default = datetime.now, blank = True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = Blogpost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = Blogpost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = Blogpost.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except Blogpost.DoesNotExist:
                pass  

        super(Blogpost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

