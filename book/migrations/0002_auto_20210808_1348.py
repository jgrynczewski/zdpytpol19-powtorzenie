# Generated by Django 3.2.6 on 2021-08-08 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.IntegerField(choices=[(1, 'Comedy'), (2, 'Thriller'), (3, 'Romance')]),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
