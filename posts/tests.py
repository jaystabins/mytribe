from django.test import TestCase, Client
from django.urls import reverse, resolve
from posts.views import PostListVeiw, PostCreateView, PostDeleteView


class TestUrls(TestCase):
    def test_list_url_resolves(self):
        url = reverse("main-feed")
        self.assertEquals(resolve(url).func.view_class, PostListVeiw)

    def test_create_url_resolves(self):
        url = reverse("new-post")
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_delete_url_resolves(self):
        url = reverse("post-delete", args=[154])
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse("main-feed")
        self.new_post_url = reverse("new-post")

    def test_post_list_view_GET(self):

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/post_list.html")

    def test_post_new_post_POST(self):

        response = self.client.post(self.new_post_url)
        self.assertEqual(response.status_code, 302)
