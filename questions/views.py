from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from .models import File, Statement, StatementTest
from django.db import transaction
from django.shortcuts import redirect
from .forms import FileForm
from django.forms import inlineformset_factory
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import StatementFormset , StatementFormsetEdit
# Create your views here.


class FileList(ListView):
    model = File


class FileCreate(CreateView):
    model = File
    fields = ['region', 'province', 'district', 'community', 'address', 'family_name',
              'intervention_sector', 'reluctant_houses', 'members', 'registration_date', 'sex']


class FileStatementMemberCreate(CreateView):
    model = File
    form_class = FileForm
    success_url = reverse_lazy('file-list')



    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['statementmembers'] = StatementFormset(self.request.POST)
        else:
            statement_tests = list(StatementTest.objects.all().values('order', 'title').order_by('order'))
            data['statementmembers'] = StatementFormset(initial=statement_tests)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        statementmembers = context['statementmembers']
        with transaction.atomic():
            self.object = form.save()

            if statementmembers.is_valid():
                statementmembers.instance = self.object
                statementmembers.save()
        return super(FileStatementMemberCreate, self).form_valid(form)



class FileUpdate(UpdateView):
    model = File
    success_url = '/'
    fields = ['region', 'province', 'district', 'community', 'address', 'family_name',
              'intervention_sector', 'reluctant_houses', 'members', 'registration_date', 'sex']


class FileStatementMemberUpdate(UpdateView):
    model = File
    form_class = FileForm
    success_url = reverse_lazy('file-list')

    def get_context_data(self, **kwargs):
        data = super(FileStatementMemberUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['statementmembers'] = StatementFormsetEdit(self.request.POST, instance=self.object)
        else:
            data['statementmembers'] = StatementFormsetEdit(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        statementmembers = context['statementmembers']
        with transaction.atomic():
            self.object = form.save()

            if statementmembers.is_valid():
                statementmembers.instance = self.object
                statementmembers.save()
        return super(FileStatementMemberUpdate, self).form_valid(form)


class FileDelete(DeleteView):
    model = File
    success_url = reverse_lazy('file-list')



def file_list(request):
    files = File.objects.all()
    return render(request, 'questions/file_list.html', {'files': files})


def file_detail(request, pk):
    file = get_object_or_404(File, pk=pk)
    return render(request, 'questions/file_detail.html', {'file': file})


def file_new(request):
    if request.method == "POST":
        form = FileForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('file_detail', pk=post.pk)
    else:
        form = FileForm()
        form_set = inlineformset_factory(File, Statement, fields=('title',))
    return render(request, 'questions/file_edit.html', {'form': form, 'form_set': form_set})


def file_edit(request, pk):
    file = get_object_or_404(File, pk=pk)
    if request.method == "POST":
        form = FileForm(request.POST, instance=file)
        if form.is_valid():
            file = form.save(commit=False)
            file.save()
            return redirect('file_detail', pk=file.pk)
    else:
        form = FileForm(instance=file)
    return render(request, 'questions/file_edit.html', {'form': form})
