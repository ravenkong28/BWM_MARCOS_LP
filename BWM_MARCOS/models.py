# models.py
from django.db import models
from django.contrib.auth.models import User
     
class Kriteria(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     kode_kriteria = models.CharField(max_length=255)
     user_specific_kode_kriteria = models.CharField(max_length=255, unique=True, editable=False)
     nama_kriteria = models.CharField(max_length=255)
     jenis_kriteria = models.CharField(max_length=255)

     def save(self, *args, **kwargs):
          if not self.kode_kriteria:
               user_kriteria_count = Kriteria.objects.filter(user=self.user).count() + 1
               self.kode_kriteria = f"C{user_kriteria_count}"
               user_id_str = str(self.user.id)
               self.user_specific_kode_kriteria = f"{user_id_str} - {self.kode_kriteria}"

          super(Kriteria, self).save(*args, **kwargs)

     def __str__(self):
          return f"{self.user_specific_kode_kriteria} - {self.nama_kriteria}"
     

class Supplier(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     nama = models.CharField(max_length=255)
     alamat = models.TextField()
     nomor_telepon = models.CharField(max_length=15)
     
     def __str__(self):
          return self.nama
     
# class NilaiKriteria(models.Model):
#      nilai = models.IntegerField()
#      keterangan = models.CharField(max_length=255)

#      def __str__(self):
#           return f"{self.nilai} - {self.keterangan}"


     
