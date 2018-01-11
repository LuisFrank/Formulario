from django.contrib import admin
from .models import StatementTest, Statement, File
# Register your models here.

admin.site.register(StatementTest)
admin.site.register(Statement)
admin.site.register(File)