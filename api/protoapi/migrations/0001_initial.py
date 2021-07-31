# Generated by Django 3.1.13 on 2021-07-31 15:32
# Generated models must be modified to set 'managed' : True

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('idrecord', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.PositiveBigIntegerField()),
                ('ammount', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'record',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('idtype', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('iduser', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
    ]
