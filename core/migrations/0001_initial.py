# Generated by Django 4.0.6 on 2022-08-02 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('phone_number', models.CharField(default='', max_length=10, primary_key=True, serialize=False)),
                ('name_customer', models.CharField(default='', max_length=100)),
                ('date_of_birth', models.CharField(default='', max_length=10)),
                ('gender', models.BooleanField(default=True)),
                ('time', models.DateTimeField(auto_now=True, null=True)),
                ('last_login', models.DateTimeField(auto_now=True, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CountyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('county_keyword', models.CharField(default='', max_length=5)),
                ('county_name', models.CharField(default='', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParameterLR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('parameter', models.CharField(default='', max_length=255)),
                ('is_using', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField(default=0.0)),
                ('floors', models.IntegerField(default=0)),
                ('location', models.IntegerField(default=0)),
                ('to_center', models.FloatField(default=0.0)),
                ('predict_price', models.FloatField(default=0.0)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('product_name', models.CharField(default='', max_length=255)),
                ('price', models.FloatField(default=0.0)),
                ('address', models.CharField(default='', max_length=255)),
                ('image', models.TextField(default='')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.countycategory')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
