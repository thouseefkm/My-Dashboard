# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, DeleteView
from .models import Link
from .forms import LinkForm
from collections import defaultdict


class LinkDetail(DetailView):
    model = Link

def link_list(request):
    links = Link.objects.all().order_by('category')

    links_dict = defaultdict(list)
    # links_dict = {}
    for link in links:
        # if link.category in links_dict:
        links_dict[link.category].append(link)
        # else:
        #     links_dict[link.category] = [link]

    return render(request, 'link/index.html', {'links_dict': dict(links_dict)})


def link_new(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = LinkForm()
    return render(request, 'link/link_edit.html', {'form': form})


def link_edit(request, pk):
    link = get_object_or_404(Link, pk=pk)
    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            return redirect('/link/' + str(link.pk))
    else:
        form = LinkForm(instance=link)
    return render(request, 'link/link_edit.html', {'form': form})


def link_delete(request, pk):
    link = get_object_or_404(Link, pk=pk)
    link.delete()
    return redirect('/')


class LinkDelete(DeleteView):
    model = Link

    def get_success_url(self):
        return redirect('')