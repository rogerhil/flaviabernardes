from ..utils import JsonView


class CloseTopBarView(JsonView):

    def json_post(self, request, *args, **kwargs):
        request.session['enable_top_bar'] = False
        return dict(success=True, enable_top_bar=False)

