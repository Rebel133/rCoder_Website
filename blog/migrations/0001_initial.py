# Generated by Django 3.0.7 on 2020-06-09 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=155)),
                ('content', models.CharField(max_length=50)),
                ('auther', models.CharField(max_length=50)),
                ('timeStamp', models.DateField(blank=True)),
            ],
        ),
    ]
