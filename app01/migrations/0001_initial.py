# Generated by Django 2.1.1 on 2018-10-12 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('publishDate', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('authors', models.ManyToManyField(to='app01.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('dep', models.CharField(max_length=32)),
                ('province', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publish'),
        ),
    ]