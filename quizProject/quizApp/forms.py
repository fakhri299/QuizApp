from pyexpat import model
from quizApp.models import QuizModel
from django.forms import ModelForm

class QuizForm(ModelForm):
    class Meta:
        model=QuizModel
        fields='__all__'
