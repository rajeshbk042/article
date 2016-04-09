from django.views.generic.list import ListView
from django.utils import timezone
import random


from apps.home.models import Article


class ArticleListView(ListView):

    model = Article
    template_name = 'list_article.html'

    def get_context_data(self, **kwargs):
        random_idx = random.randint(0, Article._default_manager.count() - 1)
        article = Article._default_manager.all()[random_idx]
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['article'] = article
        return context

    def get_queryset(self):

        queryset = Article._default_manager.all()
        return queryset