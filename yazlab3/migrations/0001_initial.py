# Generated by Django 4.2.13 on 2024-05-21 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('birth_date', models.DateField()),
                ('interests', models.TextField()),
                ('fasttext_vectors', models.JSONField()),
                ('scibert_vectors', models.JSONField()),
                ('fasttext_tp', models.IntegerField(default=0)),
                ('fasttext_fp', models.IntegerField(default=0)),
                ('scibert_tp', models.IntegerField(default=0)),
                ('scibert_fp', models.IntegerField(default=0)),
                ('scibert_fn', models.IntegerField(default=0)),
                ('fasttext_fn', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
