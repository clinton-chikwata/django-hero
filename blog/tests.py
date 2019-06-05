from django.test import TestCase
from . models import Post
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User



class PostsTest(TestCase):
    def createPost(self, title="Avengers", content="Thanos",date_posted =timezone.now() ,author = 'albert'):
        return Post.objects.create(
            title=title,
            content=content,
            date_posted=date_posted,
            author=author
         )
    #testing the model
    def test_Posts_creation(self):
        created = self.createPost()
        self.assertTrue(isinstance(created, Post))
        self.assertEqual(created.__str__(), created.title)
        self.assertEqual(created.content, 'Thanos')
    #testing the home view

    def test_view_home(self):
        created = self.createPost()
        url = reverse('blog-home')
        resp=self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(created.author, 'albert')

    # def test_update_post(self):
    #     post = Post.objects.filter(title = 'Avengers').update(title='Endgame')
    #     # response = self.client.post(
    #     #     reverse('blog-home',kwargs={'id':post.id}), 
    #     #      {'title': 'Endgame', 'content': 'Masitula', 'date_posted':timezone.now() , 'author':'clinton'}
    #     #     )

    #     # self.assertEqual(response.status_code, 302)
    #     self.assertEqual(post.title, 'Endgame')


