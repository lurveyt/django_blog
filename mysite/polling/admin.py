from django.contrib import admin
from polling.models import Poll

class PollAdmin(admin.ModelAdmin):
    model = Poll
    list_display = ("title", "text", "score",)

admin.site.register(Poll, PollAdmin)
# Register your models here.
