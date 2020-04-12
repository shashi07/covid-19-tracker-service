from django.shortcuts import render
from django import forms
from .models import BaseData
import csv
from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required

class DataInput(forms.Form):
    file = forms.FileField()
    country = forms.ChoiceField(choices=("India","US"))

    def save(self):
        records = csv.reader(self.cleaned_data["file"])
        next(records)
        for line in records:
            input_data = BaseData()
            input_data.country = self.cleaned_data["country"]
            input_data.date = datetime.strptime(line[1], "%d/%m/%y")
            input_data.state = line[3]
            input_data.confirmed_cases = int(line[8])
            input_data.deaths = line[7]
            input_data.save()

