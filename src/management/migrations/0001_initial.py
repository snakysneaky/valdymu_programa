# Generated by Django 4.1.3 on 2022-11-07 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_date_of_issue', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('company', models.CharField(max_length=200)),
                ('contacts', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('position', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('comments', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('n', 'NEW'), ('d', 'Done'), ('o', 'On going'), ('p', 'Postponed'), ('c', 'Canceled')], help_text='status', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('bills', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.account')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.customer')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.employee')),
                ('manager', models.ForeignKey(limit_choices_to={'manager_id': True}, on_delete=django.db.models.deletion.CASCADE, to='management.project')),
                ('tasks', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.task')),
            ],
        ),
    ]
