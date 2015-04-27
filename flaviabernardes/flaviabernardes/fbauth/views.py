from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.template import loader, RequestContext

from ..utils import JsonView


class LoginJson(JsonView):

    def json_get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return dict(authenticated=True)
        form = self._get_form()
        return dict(content=self._rendered_template(request, form))

    def _rendered_template(self, request, form):
        template = loader.get_template('fbauth/login.html')
        return template.render(RequestContext(request, {'form': form}))

    def _get_form(self, data=None):
        form = AuthenticationForm(data=data)
        form.fields['username'].widget.attrs['placeholder'] = 'Username'
        form.fields['password'].widget.attrs['placeholder'] = 'Password'
        return form

    def json_post(self, request, *args, **kwargs):
        form = self._get_form(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            if user is not None and user.is_active:
                login(request, user)
        else:
            return dict(content=self._rendered_template(request, form))


class LogoutJson(JsonView):

    def json_get(self, request, *args, **kwargs):
        logout(request)
        return dict(redirect=None)

