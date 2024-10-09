# Generated by Django 5.1.1 on 2024-09-29 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_title', models.CharField(max_length=100)),
                ('Member_name', models.CharField(max_length=100)),
                ('Issue_date', models.DateField()),
                ('Return_date', models.DateField()),
                ('rental_fee', models.IntegerField()),
            ],
        ),
    ]
