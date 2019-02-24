from django.db import models
from django.contrib.auth.models import User

# Create your models here.

Siniflar = (
    ('1.sınıf', '1.sınıf'),
    ('2.sınıf', '2.sınıf'),
    ('3.sınıf', '3.sınıf'),
    ('4.sınıf', '4.sınıf'),
)

Ogretim = (
    ('1.öğretim','1.öğretim'),
    ('2.öğretim','2.öğretim'),
)

class NewUserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13,db_column='TEL',verbose_name="Tel",default='+905** *** ** **',blank=True, null=True)
    claas = models.CharField(max_length=7,choices=Siniflar,default='1.sınıf',db_column='SINIF',verbose_name="Sınıf")
    period = models.CharField(max_length=9,choices=Ogretim,default='1.öğretim',db_column='ÖĞRETİM',verbose_name="Öğretim")

    class Meta:
        verbose_name = "Kullanıcı Ayarları"
 
    def __str__(self):
        return "Kişisel Bilgiler"

class internship(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    city = models.CharField(db_column='ŞEHİR',max_length=20,verbose_name="Şehir",blank=True, null=True)
    studentid= models.CharField(db_column='ÖiD',max_length=6,verbose_name="Öğrenci no" )
    company=models.CharField(db_column='ŞİRKET',max_length=30,verbose_name="Şirket",blank=True, null=True)
    strtdate= models.DateField(db_column='BAŞLAMA T.',verbose_name="Başlama tarihi",auto_now=False, auto_now_add=False,blank=True, null=True)
    fnshdate= models.DateField(db_column='BİTİŞ T.',verbose_name="Bitiş tarihi",auto_now=False, auto_now_add=False,blank=True, null=True)
    day=models.PositiveIntegerField(db_column='GÜN',verbose_name="Yapılan gün",blank=True, null=True  )
    files= models.FileField(upload_to='uploads/',verbose_name="Ek dosyalar",blank=True, null=True)
    Currentday = models.PositiveIntegerField(db_column='GEÇERLİ GÜN',verbose_name="Geçerli gün",blank=True, null=True)
    def __str__(self):
        return self.studentid

class commission(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name='studentid')
    studentidd= models.CharField(db_column='ÖiD',max_length=6,verbose_name="Öğrenci no" )
    academician1 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='academician1') 
    academician2 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='academician2')
    academician3 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='academician3')
    files = models.FileField(upload_to='uploads/',verbose_name="Ek dosyalar",blank=True, null=True)
    currentday = models.PositiveIntegerField(db_column='GGÜN',verbose_name="Geçerli gün",blank=False, null=False )
    def __str__(self):
        return self.studentidd

