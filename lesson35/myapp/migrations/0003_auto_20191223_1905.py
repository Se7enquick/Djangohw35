# Generated by Django 2.2 on 2019-12-23 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20191223_1842'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.AddField(
            model_name='article',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Article'),
        ),
        migrations.AddField(
            model_name='like',
            name='like',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Article'),
        ),
        migrations.AddField(
            model_name='similar',
            name='similar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Article'),
        ),
        migrations.AddField(
            model_name='topic',
            name='topic',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Article'),
        ),
    ]
