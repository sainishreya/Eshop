# Generated by Django 2.2.2 on 2019-07-08 05:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0006_auto_20190708_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('total', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('cart_product', models.ForeignKey(default=None, on_delete='CASCADE', to='MainApp.Product')),
                ('cart_user', models.ForeignKey(default=None, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
