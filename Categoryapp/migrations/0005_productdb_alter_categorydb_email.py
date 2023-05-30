# Generated by Django 4.1.7 on 2023-03-28 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Categoryapp', '0004_remove_categorydb_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(blank=True, max_length=60, null=True)),
                ('productname', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Des', models.CharField(blank=True, max_length=50, null=True)),
                ('Image', models.ImageField(upload_to='products')),
            ],
        ),
        migrations.AlterField(
            model_name='categorydb',
            name='Email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
