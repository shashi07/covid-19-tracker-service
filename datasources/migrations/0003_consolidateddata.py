# Generated by Django 3.0.5 on 2020-04-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasources', '0002_staterefreshdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsolidatedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.CharField(max_length=100)),
                ('confirmed_cases', models.IntegerField(default=0)),
                ('deaths', models.IntegerField(default=0)),
                ('recovered', models.IntegerField(default=0)),
                ('as_of_date', models.DateTimeField()),
            ],
        ),
    ]
