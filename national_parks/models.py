from django.db import models

# Create your models here.

class Park(models.Model):
    name = models.CharField(max_length=100)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return '%s, %s visited %s' % (self.name, self.state, self.visited)
