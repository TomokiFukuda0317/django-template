from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
import logging
logger = logging.getLogger(__name__)

class SampleView(View):

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        context = {
            'message': "Hello world!!",
        }
        logger.info(context)
        return render(request, 'index.html', context)

    @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        context = {
            'message': "Hello world!! by POST",
        }
        logger.info(context)
        return render(request, 'index.html', context)
