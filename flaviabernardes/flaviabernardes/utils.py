import sys, traceback

from django.views.generic import ListView, View, FormView
from django.template import RequestContext
from django.template.loader import get_template
from django import http


class JsonView(View):
    """ By using this class, the methods json_get and json_post needs to be
    implemented.
    """

    def _get_traceback(self):
        ex_type, ex, tb = sys.exc_info()
        return ''.join([str(i) for i in traceback.format_tb(tb)])

    def get(self, request, *args, **kwargs):
        try:
            data = self.json_get(request)
            return http.JsonResponse({'success': True, 'data': data})
        except Exception as err:
            msg = "%s\n%s" % (self._get_traceback(), str(err))
            return http.JsonResponse({'success': False, 'message': msg})

    def post(self, request, *args, **kwargs):
        try:
            data = self.json_post(request)
            return http.JsonResponse({'success': True, 'data': data})
        except Exception as err:
            msg = "%s\n%s" % (self._get_traceback(), str(err))
            return http.JsonResponse({'success': False, 'message': msg})

    def json_get(self, request, *args, **kwargs):
        raise NotImplementedError

    def json_post(self, request, *args, **kwargs):
        raise NotImplementedError


class JsonFormView(FormView):

    success_url = '/'
    form_template = None

    def form_valid(self, form):
        return http.JsonResponse({'success': True,
                                  'success_url': self.success_url})

    def form_invalid(self, form, extra_data=None):
        template = get_template(self.form_template)
        context = RequestContext(self.request, {'form': form})
        html = template.render(context)
        data = {'success': False, 'html': html, 'errors': form.errors}
        if extra_data:
            data.update(extra_data)
        return http.JsonResponse(data)
