# Generated by Django 3.2.12 on 2022-04-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'notes', 'verbose_name_plural': 'notes'},
        ),
        migrations.AddField(
            model_name='notes',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
