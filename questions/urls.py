from django.conf.urls import url
from questions.views import FileList, FileStatementMemberCreate, FileStatementMemberUpdate, FileDelete

urlpatterns = [
    url(r'^$', FileList.as_view(), name='file-list'),
    url(r'file/add/$', FileStatementMemberCreate.as_view(), name='file-add'),
    url(r'file/(?P<pk>[0-9]+)/$', FileStatementMemberUpdate.as_view(), name='file-update'),
    url(r'file/(?P<pk>[0-9]+)/delete/$', FileDelete.as_view(), name='file-delete'),

]

