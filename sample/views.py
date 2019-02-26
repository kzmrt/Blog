import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Post
from .forms import TestForm
from django.db.models import Q

logger = logging.getLogger('development')


class IndexView(LoginRequiredMixin, generic.ListView):

    paginate_by = 3
    template_name = 'sample/index.html'
    model = Post

    def get(self, request, *args, **kwargs):

        if self.request.GET.get('title', None):
            logger.debug("request.GET.get() = " + self.request.GET.get('title', None))

        if self.request.GET.getlist('title', None):
            logger.debug("request.GET.getlist() = " + self.request.GET.getlist('title', None)[0])

        return generic.ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('title', None):
            logger.debug("self.request.POST.get() = " + self.request.POST.get('title', None))

        if self.request.POST.getlist('title', None):
            logger.debug("self.request.POST.getlist() = " + self.request.POST.getlist('title', None)[0])

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        test_form = TestForm() # フォーム
        context['test_form'] = test_form

        return context

    def get_queryset(self):

        # 検索条件
        condition_user = Q()
        condition_title = Q()
        title = "";

        current_user = self.request.user # 現在のユーザを取得
        if current_user.is_superuser:  # スーパーユーザではない場合
            condition_user = Q(author=current_user.id)
        if title: # タイトルが指定されている場合
            condition_title = Q(title__icontains=title)

        return Post.objects.select_related().filter(condition_user & condition_title)
