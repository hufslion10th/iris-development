# Generated by Django 4.0.3 on 2022-06-01 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sepal_length', models.FloatField()),
                ('sepal_width', models.FloatField()),
                ('petal_length', models.FloatField()),
                ('petal_width', models.FloatField()),
                ('classification', models.CharField(max_length=45)),
                ('ml_algorithm', models.CharField(default='default', max_length=60)),
                ('ml_param', models.CharField(default='default', max_length=60)),
                ('username', models.CharField(default='admin', max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.preduser')),
            ],
        ),
    ]
