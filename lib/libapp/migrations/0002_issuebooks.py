# Generated by Django 4.2 on 2023-04-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=100)),
                ('student_id', models.CharField(blank=True, max_length=100)),
                ('book_name', models.CharField(max_length=200)),
                ('issued_date', models.DateField(auto_now=True)),
            ],
        ),
    ]