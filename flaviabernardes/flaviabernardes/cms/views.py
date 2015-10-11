from django.contrib.contenttypes.models import ContentType
from django.views.generic import DetailView

from ..utils import JsonView


class CmsDraftPublishView(JsonView, DetailView):

    def get_queryset(self):
        app = self.kwargs['app']
        model = self.kwargs['draft_model']
        ct = ContentType.objects.get(app_label=app, model=model)
        return ct.model_class().objects.all()

    def json_post(self, request, *args, **kwargs):
        obj = self.get_object()
        publish_old = bool(request.POST.get('publish_old', False))
        try:
            obj.publish(publish_old)
        except self.model.TooOldToPublish as err:
            return {'too_old': str(err)}
        return {}



class CmsObjectNewDraftView(JsonView, DetailView):

    def get_queryset(self):
        app = self.kwargs['app']
        model = self.kwargs['model']
        ct = ContentType.objects.get(app_label=app, model=model)
        return ct.model_class().objects.all()

    def json_post(self, request, *args, **kwargs):
        obj = self.get_object()
        draft = obj.new_draft()
        return {'draft_id': draft.id}
