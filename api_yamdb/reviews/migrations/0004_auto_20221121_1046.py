# Generated by Django 2.2.16 on 2022-11-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20221105_1714'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='unuque_user_make_review',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Текст комментария'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Название жанра'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(verbose_name='Текст отзыва'),
        ),
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Название произведения'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_user_make_review'),
        ),
    ]