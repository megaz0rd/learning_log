from django.db import models


class Topic(models.Model):
    """Topic is being learned by user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns model representation as a text string"""
        return self.text


class Entry(models.Model):
    """Specific informations about a progress in learning"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns model representation as a text string"""
        return f"{self.text[:50]}..."
