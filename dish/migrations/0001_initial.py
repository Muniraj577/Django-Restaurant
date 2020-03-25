# Generated by Django 3.0 on 2020-03-25 03:23

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('name',))),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='dish/images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Category.Category')),
            ],
            options={
                'verbose_name': 'dish',
                'verbose_name_plural': 'dishes',
            },
        ),
    ]
