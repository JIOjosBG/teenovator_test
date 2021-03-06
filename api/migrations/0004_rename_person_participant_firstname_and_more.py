# Generated by Django 4.0.4 on 2022-05-04 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_participant_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='person',
            new_name='firstName',
        ),
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='participant',
            name='lastName',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='registered_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together={('firstName', 'lastName', 'project')},
        ),
    ]
