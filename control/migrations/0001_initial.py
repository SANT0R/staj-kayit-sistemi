# Generated by Django 2.1.2 on 2019-01-02 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='commission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Currentday', models.PositiveIntegerField(blank=True, db_column='GGÜN', null=True, verbose_name='Geçerli gün')),
                ('files', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Ek dosyalar')),
                ('academician1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academician1', to=settings.AUTH_USER_MODEL)),
                ('academician2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academician2', to=settings.AUTH_USER_MODEL)),
                ('academician3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academician3', to=settings.AUTH_USER_MODEL)),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, db_column='ŞEHİR', max_length=20, null=True, verbose_name='Şehir')),
                ('company', models.CharField(blank=True, db_column='ŞİRKET', max_length=30, null=True, verbose_name='Şirket')),
                ('strtdate', models.DateField(blank=True, db_column='BAŞLAMA T.', null=True, verbose_name='Başlama tarihi')),
                ('fnshdate', models.DateField(blank=True, db_column='BİTİŞ T.', null=True, verbose_name='Bitiş tarihi')),
                ('day', models.PositiveIntegerField(blank=True, db_column='GÜN', null=True, verbose_name='Yapılan gün')),
                ('files', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Ek dosyalar')),
                ('Currentday', models.PositiveIntegerField(blank=True, db_column='GEÇERLİ GÜN', null=True, verbose_name='Geçerli gün')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, db_column='TEL', default='+905** *** ** **', max_length=13, null=True, verbose_name='Tel')),
                ('claas', models.CharField(choices=[('1.sınıf', '1.sınıf'), ('2.sınıf', '2.sınıf'), ('3.sınıf', '3.sınıf'), ('4.sınıf', '4.sınıf')], db_column='SINIF', default='1.sınıf', max_length=7, verbose_name='Sınıf')),
                ('period', models.CharField(choices=[('1.öğretim', '1.öğretim'), ('2.öğretim', '2.öğretim')], db_column='ÖĞRETİM', default='1.öğretim', max_length=9, verbose_name='Öğretim')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Kullanıcı Ayarları',
            },
        ),
    ]