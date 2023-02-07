from string import Template
from django.db import models
from django.db.models.aggregates import Sum
from django.contrib.auth.models import User


class Author(models.Model):
    """Модель, содержащая объекты всех авторов."""

    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_of_author = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.author_user}"

    def update_rating(self) -> None:
        """Обновляет рейтинг текущего автора.

        Состоит из:
        суммарный рейтинг каждой статьи автора умножается на 3;
        суммарный рейтинг всех комментариев автора;
        суммарный рейтинг всех комментариев к статьям автора."""

        # собираем все посты автора, а из них суммируем в переменную postRating рейтинг каждой
        post_rat = self.post_set.aggregate(postRating=Sum('rating_of_post'))
        # обнуляем итоговый рейтинг автора, иначе каждый раз новая сумма
        # будет прибавляться к уже сохранённому значению
        post_rat_sum = 0
        # и получаем итоговый рейтинг статей, выдернув уже посчитанную переменную postRating
        post_rat_sum += post_rat.get('postRating')

        # тут уже собираем комментарии конкретного пользователя - нашего автора
        # в остальном - аналогично
        com_rat = self.author_user.comment_set.aggregate(commentsRating=Sum('rating_of_comment'))
        com_rat_sum = 0
        com_rat_sum += com_rat.get('commentsRating')

        # чтобы получить рейтинг всех комментариев к статьям одного автора (posts_com_rat_sum) необходимо:
        # получить все статьи автора (all_author_posts),
        # в каждой из статей просуммировать рейтинг комментариев и сложить их в общий
        all_author_posts = self.post_set.all()
        posts_com_rat_sum = 0
        for post in all_author_posts:
            iter_post_com_rat = post.comment_set.aggregate(postCommentsRating=Sum('rating_of_comment'))
            _ = int(iter_post_com_rat.get("postCommentsRating"))
            posts_com_rat_sum += _

        self.rating_of_author = post_rat_sum * 3 + com_rat_sum + posts_com_rat_sum
        self.save()


class Category(models.Model):
    """Категории новостей/статей — темы, которые они отражают
    (спорт, политика, образование и т. д.).
    Имеет единственное поле: название категории."""

    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Post(models.Model):
    """Эта модель должна содержать в себе статьи и новости, которые создают пользователи.
    Каждый объект может иметь одну или несколько категорий."""

    NEWS = 'NWS'
    ARTICLE = 'ART'

    CHOICES = [
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    ]

    author_of_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=3, choices=CHOICES, default=ARTICLE)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating_of_post = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.title}"

    def preview(self) -> str:
        """Возвращает начало статьи (предварительный просмотр) длиной 124 символа
        и добавляет многоточие в конце."""

        # Template-стрингу возвращаю по наводке из вэбинара от уважаемого Семёна Березовского,
        # если я верно понял о чём идёт речь
        template_string = Template('$prev ...')
        preview_example = self.text[:125]
        result_string = template_string.substitute(prev=preview_example)
        return result_string

    def like(self) -> None:
        """Увеличивает рейтинг статьи/новости на единицу."""

        self.rating_of_post += 1
        self.save()

    def dislike(self) -> None:
        """Уменьшает рейтинг статьи/новости на единицу."""

        self.rating_of_post -= 1
        self.save()


class PostCategory(models.Model):
    """Промежуточная модель для связи «многие ко многим»:
    - связь «один ко многим» с моделью Post;
    - связь «один ко многим» с моделью Category."""

    post_through = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_through = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Post: {self.post_through}, Category: {self.category_through}"


class Comment(models.Model):
    """Под каждой новостью/статьёй можно оставлять комментарии,
    поэтому необходимо организовать их способ хранения тоже."""

    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    rating_of_comment = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.text}"

    def like(self) -> None:
        """Увеличивает рейтинг комментария на единицу."""

        self.rating_of_comment += 1
        self.save()

    def dislike(self) -> None:
        """Уменьшает рейтинг комментария на единицу."""

        self.rating_of_comment -= 1
        self.save()
