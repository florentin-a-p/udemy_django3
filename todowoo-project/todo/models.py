from django.db import models
from django.contrib.auth.models import User

# Create your models here, as far as it has what we will need

# - name
# - box where ppl can fill in memos [v]
# - check whether the memos are important or not
# - mark the time the memos are completed [v]
# - when people create the object so [v]
#   they can rank and show the oldest things first 
#   and newest things down at the bottom

class ProjectTodoWooFlo(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    memo_box = models.TextField(blank=True)
    # user_name = models.CharField(max_length=100, blank=True)
    user_email = models.EmailField(max_length=250)   
    memo_created_date = models.DateTimeField(auto_now_add=True)
    memo_complete_date = models.DateTimeField(null=True,auto_now=True,blank=True)
    important = models.BooleanField(default=False)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
