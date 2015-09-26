from django.db import models

from image_cropping import ImageRatioField


class BasePost(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='uploads')
    listing = ImageRatioField('image', '300x300')

    class Meta:
        abstract = True

    def __str__(self):
        return '%s: %s' % (self.__class__.__name__, self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_view', None, {'slug': self.slug})


class Post(BasePost):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    published = models.BooleanField(default=False)

    def new_draft(self):
        draft = Draft.objects.create(
            title=self.title,
            slug=self.slug,
            text=self.text,
            created=self.created,
            tags=self.tags,
            image=self.image,
            listing=self.listing,
            post=self
        )
        return draft


class Draft(BasePost):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=64)
    post = models.ForeignKey(Post, null=True, blank=True, editable=False)

    def publish(self):
        post = self.post
        new = False
        if post is None:
            new = True
            post = Post()
        post.title = self.title
        post.text = self.text
        post.slug = self.slug
        post.tags = self.tags
        post.image = self.image
        post.listing = self.listing
        post.save()
        if new:
            self.post = post
            self.save()


class BaseImage(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(blank=True, upload_to='uploads')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Image(BaseImage):
    post = models.ForeignKey(Post, related_name='images')
    ratio = ImageRatioField('image', '50x50')


class DraftImage(BaseImage):
    draft = models.ForeignKey(Draft)
    ratio = ImageRatioField('image', '50x50')
