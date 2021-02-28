from django.db import models


class Topic(models.Model):
    """Topic is being learned by user"""
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns model representation as a text string"""
        return self.text
