# Generated by Django 4.1.5 on 2023-02-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kundalik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaqt', models.CharField(max_length=100)),
                ('malumot', models.TextField()),
                ('holat', models.CharField(choices=[('Boshlandi', 'Boshlandi'), ('Bajarilmoqda', 'Bajarilmoqda'), ('Bajarildi', 'Bajarildi')], max_length=100)),
            ],
        ),
    ]
