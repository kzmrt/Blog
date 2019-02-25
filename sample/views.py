import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Post
from django.db.models import Q

logger = logging.getLogger('development')


class IndexView(LoginRequiredMixin, generic.ListView):

    # paginate_by = 3
    template_name = 'sample/index.html'
    model = Post

    # def get(self, request, *args, **kwargs):
    #     self.object = None
    #     return generic.ListView.get(self, request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     self.form = self.get_form(self.form_class)
    #
    #     logger.debug("test = " + self.request.POST.get('title', None))
    #
    #     form_value = [
    #         self.request.POST.get('title', None),
    #         self.request.POST.get('authorName', None),
    #         self.request.POST.get('material', None),
    #         self.request.POST.get('start_date', None),
    #         self.request.POST.get('end_date', None),
    #     ]
    #     request.session['form_value'] = form_value
    #
    #     # Whether the form validates or not, the view will be rendered by get()
    #     return self.get(request, *args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

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
