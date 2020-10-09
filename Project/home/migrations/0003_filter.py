# Generated by Django 3.1.2 on 2020-10-09 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201008_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.CharField(choices=[('symbol', 'Symbol: A-Z'), ('-symbol', 'Symbol: Z-A'), ('-price', 'Price: High to Low'), ('price', 'Price: Low to High')], default=('symbol', 'Symbol: A-Z'), max_length=20)),
            ],
        ),
    ]
