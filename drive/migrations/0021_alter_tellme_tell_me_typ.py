# Generated by Django 3.2.13 on 2022-04-15 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0020_alter_tellme_select'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tellme',
            name='tell_me_typ',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drive.tellmetype'),
        ),
    ]
