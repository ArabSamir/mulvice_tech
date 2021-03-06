# Generated by Django 3.1.7 on 2021-02-28 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_param_activ'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('param', models.ManyToManyField(blank=True, null=True, to='website.Param')),
            ],
        ),
    ]
