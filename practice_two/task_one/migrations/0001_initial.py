# Generated by Django 4.2.2 on 2024-01-11 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableWithResultsCoinToss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_coin_toss', models.CharField(max_length=5)),
                ('time_throw', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]