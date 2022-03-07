# Generated by Django 4.0.3 on 2022-03-07 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles_page', '0003_alter_articles_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mini_description', models.CharField(max_length=217)),
                ('main_article', models.TextField()),
                ('img', models.ImageField(upload_to='images/')),
                ('url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
    ]