from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    class Estatus(models.TextChoices):
        BORRADOR = "BD", "Borrador"
        PUBLICADO = "PB", "PUBLICADO"

    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_post"
    )

    body = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    estatus = models.CharField(max_length=2, choices=Estatus, default=Estatus.BORRADOR)

    class Meta:
        ordering = ["-publicado"]

        indexes = [
            models.Index(fields=["-publicado"]),
        ]

    def __str__(self):
        return self.titulo


class PostFavorito(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey("blog.Post", on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)

    pk = models.CompositePrimaryKey("user_id", "post_id")
