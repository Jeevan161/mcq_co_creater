# Generated by Django 4.2.17 on 2025-01-21 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='models.course')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
                ('session_name', models.CharField(max_length=255, unique=True)),
                ('outcomes', models.TextField()),
                ('reading_material', models.TextField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='models.topic')),
            ],
        ),
    ]
