from django.contrib import admin
from siteapp.models import (Post,
                            ConsultationDate,
                            Category,
                            File,
                            GroupPage,
                            StartPage,
                            Theme)

admin.site.register(Post)
admin.site.register(ConsultationDate)
admin.site.register(Category)
admin.site.register(File)
admin.site.register(GroupPage)
admin.site.register(StartPage)
admin.site.register(Theme)
