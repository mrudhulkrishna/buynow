# Generated by Django 4.2.1 on 2023-06-20 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commen', '0003_customer'),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name=200)),
                ('pro_num', models.BigIntegerField()),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(upload_to='seller/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commen.seller')),
            ],
        ),
    ]