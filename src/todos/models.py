from django.db import models

STATUS_CHOICES = (
        ('I', 'In Progress'),
        ('C', 'Completed'),
        ('P', 'Pending'),
    )

class ToDo(models.Model):
    """ ToDo Model """
    title = models.CharField(max_length = 200,verbose_name='Title')
    description = models.TextField(verbose_name = "Description",null=True,blank=True)
    date = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("ToDo")
        verbose_name_plural = ("ToDos")
