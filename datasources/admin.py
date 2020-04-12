from django.contrib import admin
from django.contrib.admin import AdminSite
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from .models import BaseData
import csv
from datetime import datetime
import io
from django.contrib.admin.views.decorators import staff_member_required


class DataInput(forms.Form):
    file = forms.FileField()
    country = forms.ChoiceField(choices=(("India", "India"),("US","US")))

    def save(self):
        records = csv.reader(io.TextIOWrapper(self.cleaned_data["file"].file))
        for line in records:
            input_data = BaseData()
            input_data.country = self.cleaned_data["country"]
            input_data.date = datetime.strptime(line[1], "%d/%m/%y")
            input_data.state = line[3]
            input_data.confirmed_cases = int(line[8])
            input_data.deaths = line[7]
            input_data.save()

class CustomAdminSite(AdminSite):

     def get_urls(self):
         from django.urls import path
         urls = super().get_urls()
         urls += [
             path('my_view/', self.admin_view(self.import_data))
         ]
         return urls

     def import_data(self, request):
         if request.method == "POST":
             form = DataInput(request.POST, request.FILES)
             print(form.is_valid())
             if form.is_valid():
                 form.save()
                 success = True
                 context = {"form": form, "success": success}
                 return render(request, "imported.html", context)
         else:
             form = DataInput()
             context = {"form": form}
             return render(request, "imported.html", context)


admin_site = CustomAdminSite()


admin_site.register(BaseData)
