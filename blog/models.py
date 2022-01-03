from django.db import models
from django.conf import settings
from django.utils import timezone                                       # kunai kunai field lai timestamps rakhnu parne vayea timezone lai import gareko
from django.utils.translation import gettext_lazy as _


# this function is being used while uploading the posts image
def upload_to(instance, filename):                          # yo line ko instance vannale current post object or instance vanni bujincha
    return 'posts/{filename}'.format(filename=filename)



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    # PostObjects Class chai hamile banako Custom Manager Class ho
    class PostObjects(models.Manager):

        def get_queryset(self):
            return super().get_queryset() .filter(status='published')


    options = (                                                         # staus field ko lagi drop down facility use garna yesari dropdown to lagi options diyeko
        ('draft', 'Draft'),
        ('published', 'Published'),
    )


    category = models.ForeignKey(Category, related_name='posts', on_delete=models.PROTECT, default=1)             # models.PROTECT won't allow you to delete the category
    title = models.CharField(max_length=250)
    image = models.ImageField(_("Image"), upload_to=upload_to, default='posts/default.jpg')     # yo line ko upload_to  auta custom function ho jun hamile mathi define gareko chau
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')                    # slug generally text or string which we generally uses in url to identify each items seperately(here, to identify each posts) # unique 'id' use garna vanda slug use gareko dherai ramro for the security purpose
    published = models.DateTimeField(default=timezone.now)                                  # published date
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts', default=None, null=True)
    status = models.CharField(max_length=10, choices=options, default='published')

    # yo talako manager field haru database ko table ma dekhaudaina... just hamile view ma chai use garna sakincha
    objects = models.Manager()                          # default manager   # yo line tw nalekhe pani hunthyo hola
    postobjects = PostObjects()                         # calling our created custom manager (hamro lagi banako)

    class Meta:
        ordering = ('-published',)                      # object retrieve garda published field ko value ko descending order ma hos vanera yesto gareko

    def __str__(self):
        return self.title                               # returning title as string
