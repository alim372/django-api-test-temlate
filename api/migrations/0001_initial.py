# Generated by Django 3.0.6 on 2021-02-12 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModelApi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.TextField()),
                ('state', models.CharField(choices=[('True', 'True'), ('False', 'False'), ('Deleted', 'Deleted')], default='True', max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'test_tabel_api',
            },
        ),
    ]