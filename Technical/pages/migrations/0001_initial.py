# Generated by Django 3.1.3 on 2020-11-14 22:15

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
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pretest', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True)),
                ('posttest', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True)),
                ('codingProject', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True)),
                ('finalGrade', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grade', to=settings.AUTH_USER_MODEL, unique=None)),
            ],
        ),
    ]