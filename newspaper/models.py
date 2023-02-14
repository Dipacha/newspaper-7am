from django.db import models

class TimesStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at =  models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True #does not create table for TimeStampModel

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICE = (
        ("published", "Published"),
        ("unpublished", "Un-published"),
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False)
    author_at = models.ForeignKey("auth.User", on_delete=models.CASCADE)                               
    published_at =models.DateTimeField(null=True, blank=True)
    views_count= models.PositiveBigIntegerField(default=0)
    status= models.CharField(max_length=20, choices=STATUS_CHOICE, default="unpublished")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    
    def __str__(self):
        return self.title
    #Fat model and thin views
    @property
    def latest_comments(self):
        comments=Comment.objects.filter(post=self).order_by("-created_at")
        return comments

class NewsLetter(TimesStampModel):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
class Contact(TimesStampModel):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.subject

class Comment(TimesStampModel):
    subject = models.ForeignKey(Post,on_delete=models.CASCADE)
    message = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()

    
    def __str__(self):
        return self.message[:70]