# Generated by Django 3.1.3 on 2020-11-02 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_page', '0002_auto_20201102_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='title',
            field=models.CharField(default='02.11.2020', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='courseregistration',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='main_page.course'),
        ),
        migrations.AlterField(
            model_name='courseregistration',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_registrations', to='main_page.studentprofile'),
        ),
        migrations.AlterField(
            model_name='courseschedule',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='main_page.course'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lectures', to='main_page.course'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
