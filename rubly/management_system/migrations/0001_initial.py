# Generated by Django 4.2.3 on 2023-08-24 08:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=50, unique=True)),
                ('Packaging', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Description_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Goods_received',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('Quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateField()),
                ('remaining', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Project_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_system.client')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management_system.owner')),
            ],
            options={
                'unique_together': {('client', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Returns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('Quantity', models.IntegerField()),
                ('returned_by', models.CharField(max_length=50)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_system.description')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_ID', models.CharField(max_length=50, unique=True)),
                ('project_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_system.project_type')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
                ('project_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_system.project_type')),
            ],
        ),
        migrations.CreateModel(
            name='IssuanceInternal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('issuedTo', models.CharField(max_length=50)),
                ('Project', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_system.description')),
            ],
        ),
        migrations.CreateModel(
            name='IssuanceExternal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=50)),
                ('Carpex', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('remaining', models.IntegerField()),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_system.goods_received')),
            ],
        ),
        migrations.AddField(
            model_name='goods_received',
            name='Project_Type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management_system.project_type'),
        ),
        migrations.AddField(
            model_name='goods_received',
            name='Purchase_Order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='management_system.purchase_order'),
        ),
        migrations.AddField(
            model_name='goods_received',
            name='description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_system.description'),
        ),
        migrations.AddField(
            model_name='description',
            name='Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_system.description_type'),
        ),
        migrations.AlterUniqueTogether(
            name='goods_received',
            unique_together={('Purchase_Order', 'description')},
        ),
    ]
