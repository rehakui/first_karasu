from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day

"""TopPage"""
def index(request):
    context = {
      'day_list':Day.objects.all(),
    }
    return render(request, 'qa/day_list.html', context)

"""AboutPage"""
def about(request):
    return render(request, 'qa/about.html')


def add(request):
    #送信内容をもとにフォーム（DayCreateForm）を作る
    form = DayCreateForm(request.POST or None)

    #method==POST つまり、送信ボタンが押された時に入力内容に誤りがなければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('qa:index') #postの後にはredirectすること

    #通常時のページアクセスや、入力内容に誤りがあれば再度ページを表示
    context = {
      'form':form
    }
    return render(request, 'qa/day_form.html', context)


def update(request, pk):
    #urlのpk(primary key)をもとに、Dayを取得
    day = get_object_or_404(Day, pk=pk)

    #フォームに取得したDayを紐付ける
    form = DayCreateForm(request.POST or None, instance=day)

    #Trueならば、
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('qa:index')

    #Falseならば、
    context = {
      'form':form
    }
    return render(request, 'qa/day_form.html', context)



def delete(request, pk):
    #urlのpk(primary key)をもとに、Dayを取得
    day = get_object_or_404(Day, pk=pk)

    #Trueならば、
    if request.method == 'POST':
        day.delete()
        return redirect('qa:index')

    #Falseならば、
    context = {
      'day':day,
    }
    return render(request, 'qa/day_confirm_delete.html', context)


def detail(request, pk):
    #urlのpk(primary key)をもとに、Dayを取得
    day = get_object_or_404(Day, pk=pk)

    context = {
      'day':day,
    }
    return render(request, 'qa/day_detail.html', context)
