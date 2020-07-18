# Generated by Django 2.0.2 on 2020-07-18 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ece', '0004_members_yr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='achievements')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('achievement', models.TextField(null=True)),
                ('yr', models.IntegerField(null=True)),
                ('fb', models.URLField(null=True)),
                ('ln', models.URLField(null=True)),
            ],
        ),
    ]
