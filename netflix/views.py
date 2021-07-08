from django.views.generic.base import TemplateView

from .models import Video

class IndexView(TemplateView):
    template_name = "netflix/index.html"


class PlayView(TemplateView):
    template_name = "netflix/play.html"

    def get_context_data(self, **kwargs):
        context = super(PlayView, self).get_context_data(**kwargs)
        context['video'] = Video.objects.get(pk=kwargs['video_id'])
        return context

 