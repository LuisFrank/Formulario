from django.conf.urls import url
# from . import views
from questions.views import FileList, FileStatementMemberCreate, FileStatementMemberUpdate, FileDelete, file_new
urlpatterns = [
    # url(r'^$', views.file_list, name='file_list'),
    # url(r'^file/(?P<pk>\d+)/$', views.file_detail, name='file_detail'),
    # url(r'^file/new/$', file_new, name='file_new'),
    # url(r'^file/(?P<pk>\d+)/edit/$', views.file_edit, name='file_edit'),
    url(r'^$', FileList.as_view(), name='file-list'),
    url(r'file/add/$', FileStatementMemberCreate.as_view(), name='file-add'),
    url(r'file/(?P<pk>[0-9]+)/$', FileStatementMemberUpdate.as_view(), name='file-update'),
    url(r'file/(?P<pk>[0-9]+)/delete/$', FileDelete.as_view(), name='file-delete'),


]

