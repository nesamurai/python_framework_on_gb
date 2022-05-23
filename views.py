from framework.views import View


class Homepage(View):
    def get(self, request):
        return 'GET_SUCCESS'

    def post(self, request):
        return 'POST_SUCCESS'
