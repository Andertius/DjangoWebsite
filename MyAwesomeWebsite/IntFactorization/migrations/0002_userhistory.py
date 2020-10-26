# Generated by Django 3.1.2 on 2020-10-17 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IntFactorization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prime_answer', models.CharField(blank=True, max_length=9999, null=True)),
                ('knapsack_answer', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='IntFactorization.useracc')),
            ],
        ),
    ]
