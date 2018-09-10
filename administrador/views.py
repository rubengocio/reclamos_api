from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader
from django.urls import reverse
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


class ReclamoListView(LoginRequiredMixin, View):

    def get(self, request):
        template = loader.get_template('reclamos.html')
        reclamos = Reclamo.objects.all()
        #page = request.GET.get('page', 1)
        #paginator = Paginator(reclamos, 10)

        #try:
        #    reclamos = paginator.page(page)
        #except PageNotAnInteger:
        #    reclamos = paginator.page(1)
        #except EmptyPage:
        #    reclamos = paginator.page(paginator.num_pages)

        return HttpResponse(template.render({'reclamos': reclamos}, request))


class ReclamoDetailView(View):
    template_name = 'form-reclamo.html'

    def get(self, request, pk):
        reclamo = get_object_or_404(Reclamo, pk=pk)
        form = ReclamoForm(instance=reclamo)
        context={
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, pk=None):
        reclamo=None
        if pk:
            reclamo=get_object_or_404(Reclamo, pk=pk)
        form = ReclamoForm(data=request.POST, instance=reclamo)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('reclamos'))

        context={
            'form':form
        }
        return render(request, self.template_name, context)
