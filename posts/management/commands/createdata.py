from django.core.management.base import BaseCommand
from users.models import User
from posts.models import Post
from comments.models import Comment
from faker import Faker
import random
import faker.providers

class Command(BaseCommand):
    help = 'Command Information'

    def handle(self, *args, **kwargs):
        
        faker = Faker()
        for _ in range(30):
            User.objects.create(
                user_name=faker.word(),
                first_name=faker.word().title(),
                last_name=faker.word().title(),
                email= faker.email(),
                gender = faker.word(),
                relationship_status = faker.word(),
                hometown = faker.address(),
                current_location = faker.address(),
                bio = faker.paragraph(nb_sentences=6),
                password= faker.password(),
                is_staff = faker.boolean(),
                is_active = True
            ) 


        users = list(User.objects.all())

        for _ in range(50):
            Post.objects.create(
                post = faker.paragraph(nb_sentences=15),
                user = random.choice(users),
                is_public = faker.boolean()
            )

        posts = list(Post.objects.all())

        for _ in range(35):

            Comment.objects.create(
                content = faker.paragraph(nb_sentences=2),
                user = random.choice(users),
                post = random.choice(posts),
                # parent = random.choice(Comment.objects.all())
            )

        for _ in range(60):

            
            post = random.choice(posts)

            parent = Comment.objects.filter(post=post.id)

            try:
                Comment.objects.create(
                    content = faker.paragraph(nb_sentences=2),
                    user = random.choice(users),
                    post = post,
                    parent = random.choice(parent)
                )
            except:
                print('something went wrong')
