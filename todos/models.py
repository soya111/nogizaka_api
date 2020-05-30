from django.db import models
# from datetime import datetime

# Create your models here.


# class Todo(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title


class Member(models.Model):
    name = models.CharField(max_length=50)
    # hiragana_name = models.CharField(max_length=50)
    # generation = models.IntegerField()
    # birthday = models.DateField()
    # birthplace = models.CharField(max_length=50)
    # blood_type = models.CharField(max_length=2, null=True)
    # height = models.IntegerField()
    # is_graduated = models.BooleanField()
    # graduation_date = models.DateField(null=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=50)
    # hiragana_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SongMembers(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
