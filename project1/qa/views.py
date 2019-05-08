from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm, CommentCreateForm
from .models import Day, Category, Comment
from django.views import generic #汎用ビュー
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin #ログイン必須になる
from django.db.models import Q



class IndexView(generic.ListView):
    model = Day #モデル名_list.html という名でテンプレートへ渡される
    #template_name = 'qa/my_list.html' と書くことも可能
    paginate_by = 5

    def get_queryset(self):
        queryset = Day.objects.order_by('-date')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
              Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset


"""AboutPage"""
def about(request):
    return render(request, 'qa/about.html')


"""PlayerPage"""
def player(request):
    return render(request, 'qa/player.html')



class AddView(LoginRequiredMixin, generic.CreateView): #CreateViewのデフォルトで探すテンプレート名は、モデル名_form.html
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('qa:index')


class UpdateView(LoginRequiredMixin, generic.UpdateView): #デフォルトテンプレートは、モデル名_form.html
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('qa:index')


class DeleteView(LoginRequiredMixin, generic.DeleteView): #デフォルトテンプレートは、モデル名_confirm_delete.html
    model = Day
    success_url = reverse_lazy('qa:index')


class DetailView(generic.DetailView): #デフォルトテンプレートは、モデル名_detail.html
    model = Day


class CategoryView(generic.ListView):
    model = Day
    paginate_by = 5

    def get_queryset(self):
        """
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Day.objects.order_by('-date').filter(category=category)
        """
        category_pk = self.kwargs['pk']
        queryset = Day.objects.order_by('-date').filter(category__pk=category_pk)
        return queryset


class CommentView(generic.CreateView):
    model = Comment
    #fields = ('name', 'text')
    form_class = CommentCreateForm

    def form_valid(self, form):
        day_pk = self.kwargs['day_pk']
        comment = form.save(commit=False)
        comment.day = get_object_or_404(Day, pk=day_pk)
        comment.save()
        return redirect('qa:detail', pk=day_pk)
