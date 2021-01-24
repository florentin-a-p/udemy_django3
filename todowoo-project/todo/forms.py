from django.forms import ModelForm
from .models import ProjectTodoWooFlo

class TodoForm(ModelForm):
    class Meta:
        model = ProjectTodoWooFlo 
        fields = ['title','memo_box','important']
