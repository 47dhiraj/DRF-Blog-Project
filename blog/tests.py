# from django.test import TestCase                # django le diyeko TestCase lai import gareko

# from django.contrib.auth.models import User

# from blog.models import Post, Category          # jun jun models ko data lai test garni ho tyo model lai test gareko

# # Note : yo talako testing garda hamro real database ko data ma kei change aaudaina because yesle chutai fake database create garcha
# # yo talako sabbai kura chai models.py or model lai test garna ko lagi.. model le ramro sanga kaam gari rako cha ki nai vanera test garna lai
# # when we run command in terminal ==> coverave run --omit = '*/venv/*' manage.py test     ..  yo Test_Create_Post class ko sabbai function haru automatic call huncha kasaile call garna pardaina.. so yesari model testing huncha

# class Test_Create_Post(TestCase):

#     @classmethod
#     def setUpTestData(cls):             # fake or testing databae ko table ma fake object create garera halna ko lagi hamile custom definition of function banako & tesma tei anusar code lekheko
#         test_category = Category.objects.create(name='django')
#         testuser1 = User.objects.create_user(username='test_user1', password='123456789')
#         test_post = Post.objects.create(category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published')

#     def test_blog_content(self):        # fake or testing database table batw object lai retireve gareko & pahila haleko value cha ki nai vanera checking pani gareko cha using assertEqual() method
#         post = Post.postobjects.get(id=1)
#         cat = Category.objects.get(id=1)
#         author = f'{post.author}'
#         excerpt = f'{post.excerpt}'
#         title = f'{post.title}'
#         content = f'{post.content}'
#         status = f'{post.status}'
#         self.assertEqual(author, 'test_user1')
#         self.assertEqual(title, 'Post Title')
#         self.assertEqual(content, 'Post Content')
#         self.assertEqual(status, 'published')
#         self.assertEqual(str(post), "Post Title")
#         self.assertEqual(str(cat), "django")
