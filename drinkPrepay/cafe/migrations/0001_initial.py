# Generated by Django 4.1.2 on 2022-11-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('count', models.PositiveIntegerField()),
                ('status', models.SmallIntegerField(choices=[(0, '下架'), (1, '上架')], default=1)),
            ],
        ),
    ]
