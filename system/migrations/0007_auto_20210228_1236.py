# Generated by Django 3.1.1 on 2021-02-28 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_auto_20210228_0653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='Select genres for this book', null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.genre'),
        ),
    ]