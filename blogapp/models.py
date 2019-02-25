from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body= models.TextField()


#blog object라고 써져있는거 바꾸고싶을때
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]