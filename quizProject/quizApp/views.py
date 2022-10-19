from django.shortcuts import redirect, render
from quizApp.models import QuizModel
from quizApp.forms import QuizForm

# Create your views here.
def home(request):
    if request.method=='POST':
        questions=QuizModel.objects.all()
        correct=0
        wrong=0
        total=0
        for q in questions:
            total+=1
            if q.ans== request.POST.get(q.question):
                correct+=1
            else:
                wrong+=1
        context={
            'correct':correct,
            'wrong':wrong,
            'total':total,

        }
        return render(request,'result.html',context)

    else:
        questions=QuizModel.objects.all()
        context={'questions':questions}
        return render(request,'home.html',context)


def addquestion(request):
    form=QuizForm()
    if request.method=='POST':
        form=QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addquestion')
    context={'form':form}

    return render(request,'addquestion.html',context)

