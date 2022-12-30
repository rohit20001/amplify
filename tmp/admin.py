from django.contrib import admin
from tmp.models import Post,Project,New_Student,extendedUser,Course,Paid_Student,Story,Certi
from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_upper_para','content_lower_para', 'posted_date','postedBy')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('head', 'content', 'posted_date_project','postedBy_project')

class New_StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact','dob','sub','When_contacted')

class extendedUserAdmin(admin.ModelAdmin):
    list_display = ('phone','email')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name','course_image','course_teacher','Features_of_courses','posted_date','fees','aboutTeacher')

class Paid_StudentAdmin(admin.ModelAdmin):
    list_display = ('username','name','course_name','course','amount','payment_id','paid','purchased_date')

class StoryAdmin(admin.ModelAdmin):
    list_display = ('story_image','brief_content','story_by')

class CertiAdmin(admin.ModelAdmin):
    list_display = ('certi_id','cert_name','cert_for','cert_collegeName','issue_date')



# For certificates

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class CertiAdmin(admin.ModelAdmin):
    list_display = ('certi_id','cert_name','cert_for','cert_collegeName','issue_date')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Certi.objects.update_or_create(
                    certi_id = fields[0],
                    cert_name = fields[1],
                    cert_for = fields[2],
                    cert_collegeName = fields[3],
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Certi, CertiAdmin)



admin.site.register(Post, PostAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(New_Student,New_StudentAdmin)
admin.site.register(extendedUser,extendedUserAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Paid_Student,Paid_StudentAdmin)
admin.site.register(Story,StoryAdmin)
