# Generated by Django 4.1.3 on 2024-12-14 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('bio', models.CharField(max_length=400)),
                ('profile_image_url', models.TextField(default='https://www.shutterstock.com/image-vector/avatar-photo-default-user-icon-600nw-2345549599.jpg')),
                ('email', models.CharField(max_length=150)),
                ('created_on', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('uid', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postcategory', to='rareapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('publication_date', models.DateField()),
                ('image_url', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=500)),
                ('approved', models.BooleanField(default=True)),
                ('category', models.ManyToManyField(to='rareapi.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('created_on', models.DateField()),
                ('author_id', models.ForeignKey(null='false', on_delete=django.db.models.deletion.CASCADE, to='rareapi.user')),
                ('post_id', models.ForeignKey(null='false', on_delete=django.db.models.deletion.CASCADE, to='rareapi.post')),
            ],
        ),
    ]
