# Generated by Django 3.1.1 on 2020-09-30 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kindergartens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kindergarten',
            name='after_school',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='after_school_inclusion',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='all_day',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='cooperation',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='corporate',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='culture',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='disabled',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='disabled_integration',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='extension',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='family',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='general',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='grade',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='has_extension_class',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='holiday',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='infants',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='language',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='office',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='other',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='part_time',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='private',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='public',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='school_bus',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='science',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='sport',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='welfare',
            field=models.BooleanField(),
        ),
    ]
