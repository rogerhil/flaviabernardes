from django.db import models

from image_cropping import ImageRatioField


class BaseBlog(models.Model):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.TextField(null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='uploads')
    listing = ImageRatioField('image', '300x300')

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
        self.blog.tags = self.tags
        self.blog.save()


class BaseImage(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(blank=True, upload_to='uploads')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Image(BaseImage):
    blog = models.ForeignKey(Blog, related_name='images')
    ratio = ImageRatioField('image', '50x50')


class DraftImage(BaseImage):
    draft = models.ForeignKey(Draft)
    ratio = ImageRatioField('image', '50x50')
