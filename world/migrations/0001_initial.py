# Generated by Django 3.0.4 on 2020-04-06 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=15)),
                ('road', models.CharField(max_length=15)),
                ('boundaries', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_data', models.DateField()),
                ('session', models.IntegerField(verbose_name='规委会期数')),
                ('notes', models.TextField(max_length=1000, verbose_name='会议纪要')),
                ('grade', models.CharField(max_length=15, verbose_name='市级or 管委会？')),
            ],
        ),
        migrations.CreateModel(
            name='ConstructionUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corp_name', models.CharField(max_length=200, unique=True)),
                ('introduction', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('section', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='DesignInstitute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corp_name', models.CharField(max_length=200, unique=True)),
                ('introduction', models.TextField(max_length=500)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('section', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=15)),
                ('intro', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ExpertReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.Department')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewCom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_leader', models.BooleanField(default=False)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.Expert')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.ExpertReview')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('intro', models.TextField(max_length=500)),
                ('addr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.Address')),
                ('commission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.Commission')),
                ('construction_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.ConstructionUnit')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.DesignInstitute')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.ExpertReview')),
            ],
        ),
        migrations.AddField(
            model_name='expertreview',
            name='experts',
            field=models.ManyToManyField(through='world.ReviewCom', to='world.Expert'),
        ),
        migrations.AddField(
            model_name='expertreview',
            name='staffs',
            field=models.ManyToManyField(to='world.Staff'),
        ),
        migrations.AddField(
            model_name='constructionunit',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.Contact'),
        ),
    ]