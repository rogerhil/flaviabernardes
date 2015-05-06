from django.db import models

from image_cropping import ImageRatioField


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return '%s' % self.name


class BaseBlog(models.Model):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #head_image = models.ForeignKey('HeadImage')
    tags = models.ManyToManyField(Tag)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})


class Blog(BaseBlog):
    published = models.BooleanField(default=False)


class Draft(BaseBlog):
    blog = models.ForeignKey(Blog)

    def publish(self):
        self.blog.title = self.title
        self.blog.text = self.text
        self.blog.slug = self.slug
        #self.blog.head_image = self.head_image
        #self.tags.clean()
        self.blog.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return '%s' % self.name


class BaseImage(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(blank=True, upload_to='uploads')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class HeadImage(BaseImage):
    head_ratio = ImageRatioField('image', '960x250')


class Image(BaseImage):
    blog = models.ForeignKey(Blog)
    ratio = ImageRatioField('image', '50x50')


class DraftImage(BaseImage):
    draft = models.ForeignKey(Draft)
    ratio = ImageRatioField('image', '50x50')
