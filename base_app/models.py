from django.db import models
from django.conf import settings

# Create your models here.
class TODO(models.Model):
    status_choices = [
        ('✔️', 'Complete'),
        ('🕒', 'Pending')
    ]
    
    priority_choices = [(i,i) for i in range (1,21)]
    
    
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices = status_choices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(max_length=2, choices = priority_choices)
    
    class Meta:
        unique_together = (
            ('user', 'priority'),
            ('user', 'title')
        )
    
    def __str__(self):
        return self.title