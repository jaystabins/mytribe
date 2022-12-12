from django.test import TestCase, Client
from django.urls import reverse, resolve
from users.views import UserDetailView, UserEditView
from posts.views import PostListVeiw, PostCreateView


class TestUrls(TestCase):
    def test_list_url_resolves(self):
        url = reverse("main-feed")
        self.assertEquals(resolve(url).func.view_class, PostListVeiw)

    def test_list_url_resolves(self):
        url = reverse("new-post")
        self.assertEquals(resolve(url).func.view_class, PostCreateView)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse("main-feed")

    def test_post_list_view_GET(self):

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/post_list.html")
