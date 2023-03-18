from django.db import models
from autoslug import AutoSlugField
# from mebel.models import Mebel
# Create your models here.


VIA = (
    ('kuxni','Kuxni'),
    ('mehmonxona',"Mehmonxona"),
    ('devan','Devan'),
    ('shkaf','Shkaf'),
    ('bolalar','Bolalar'),
    ('romlar',"Romlar")
)

publish = (
    ('active','Activ'),
    ('deactiv','Deactiv')
)



class Mebel(models.Model):
    name = models.CharField(max_length=41,null=True)
    slug = AutoSlugField(populate_from='name',unique=True)
    addres = models.CharField(max_length=100)
    narx = models.PositiveIntegerField()
    chegirma = models.PositiveIntegerField(default=0)
    like = models.PositiveIntegerField(default=0,null=True,blank=True)
    razmer = models.CharField(max_length=112,help_text="bo'yi,eni,qalinligi")
    body = models.TextField()
    turi = models.CharField(max_length=31,choices=VIA, default='kuxni')
    rangi = models.CharField(max_length=41,help_text="masalan: oq,qora,qizil,sariq")
    photo = models.ImageField(upload_to="rasm")

    status = models.CharField(max_length=31,choices=publish, default='active')
    created_at = models.DateTimeField(auto_now=True)
    updatead = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Uy jihozi'
        verbose_name_plural = 'Uy jihozlari'
        ordering = ('-created_at','status')

    def __str__(self) -> str:
        return self.name


    @property
    def add_narx(self):
        if self.chegirma:
            hisoblash = int(self.narx)-(int(self.narx) / 100) * int(self.chegirma)
            # chegirma_narxi = self.narx - self.chegirma
            return hisoblash 
    if add_narx == 0:
        chegirma_narxi = '0'
    else:
        chegirma_narxi = add_narx



class Photo(models.Model):
    model = models.ForeignKey(Mebel,on_delete=models.CASCADE,related_name="imagine")
    image = models.ImageField(upload_to='sinov',blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name="Yaratilgan vaqti")

    def __str__(self):
        return self.model.name



class Savat(models.Model):
    product = models.ForeignKey(Mebel,on_delete=models.CASCADE)
    miqdori = models.PositiveIntegerField(default=0)
    summa = models.PositiveIntegerField()

    status = models.CharField(max_length=31,choices=publish,default='active')
    created_at = models.DateTimeField(auto_now=True)
    updatead = models.DateTimeField(auto_now_add=True)

    # def __str__(self) -> str:
    #     return self.product.name
