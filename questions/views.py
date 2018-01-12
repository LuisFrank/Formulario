from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import File, StatementTest
from .forms import FileForm, StatementFormset , StatementFormsetEdit
# Create your views here.


class FileList(ListView):
    model = File
    queryset = File.objects.order_by('-created_date')


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
        return super().form_valid(form)


class FileStatementMemberUpdate(UpdateView):
    model = File
    form_class = FileForm
    success_url = reverse_lazy('file-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
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
        return super().form_valid(form)


class FileDelete(DeleteView):
    model = File
    success_url = reverse_lazy('file-list')
