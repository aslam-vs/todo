from django.contrib import admin

from .models import ToDo,STATUS_CHOICES


class ToDoAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ('title', 'description', 'date', 'status')
    search_fields = ('title', 'description', 'date')
    list_filter = ('status','active')


    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        meta = self.model._meta
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(["title", "description", "date", "status"])
        for t in queryset:
            writer.writerow([t.title, t.description, t.date, t.get_status_display()])
        return response

    download_csv.short_description = "Download CSV file for selected todos."

admin.site.register(ToDo, ToDoAdmin)