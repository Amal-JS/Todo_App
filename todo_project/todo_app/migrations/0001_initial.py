# Generated by Django 4.2.2 on 2023-07-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Test DB',
            },
        ),
    ]
