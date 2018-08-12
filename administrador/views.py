from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader
from django.utils import timezone
from datetime import timedelta

from django.views import View

from administrador.forms import ReclamoForm
from api.models import Reclamo


@login_required
def index(request):
    template = loader.get_template('index.html')

    some_day_last_week = timezone.now().date() - timedelta(days=7)

    reclamos = Reclamo.objects.filter(created_at__gte=some_day_last_week)

    reclamos = reclamos.values('created_at').annotate(total=Count('created_at')).order_by('total')


    return HttpResponse(template.render({}, request))


class ReclamoListView(View):

    def get(self, request):
        template = loader.get_template('reclamos.html')
        reclamos = Reclamo.objects.all()
        return HttpResponse(template.render({'reclamos': reclamos}, request))


class ReclamoDetailView(View):

    def get(self, request, pk):
        template = loader.get_template('form-reclamo.html')
        reclamo = get_object_or_404(Reclamo, pk=pk)
        form = ReclamoForm(instance=reclamo)
        return HttpResponse(template.render({'form': form}, request))