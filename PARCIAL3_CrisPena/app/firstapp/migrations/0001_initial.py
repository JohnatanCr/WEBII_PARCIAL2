# Generated by Django 3.0.3 on 2020-03-14 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=45)),
                ('abrev', models.CharField(max_length=16)),
                ('abrev_pm', models.CharField(max_length=16)),
                ('id_country', models.IntegerField(blank=True, null=True)),
                ('risk', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
            options={
                'db_table': 'estados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieid', models.CharField(db_column='MovieID', max_length=10, primary_key=True, serialize=False)),
                ('movietitle', models.CharField(db_column='MovieTitle', max_length=30)),
                ('releasedate', models.DateField(db_column='ReleaseDate')),
                ('genereid', models.CharField(blank=True, db_column='GenereID', max_length=10, null=True)),
                ('directorid', models.CharField(blank=True, db_column='DirectorID', max_length=10, null=True)),
                ('imageurl', models.CharField(db_column='ImageUrl', max_length=250)),
                ('description', models.CharField(db_column='Description', max_length=250)),
            ],
            options={
                'db_table': 'movie',
                'managed': False,
            },
        ),
    ]
