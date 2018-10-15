from django.db import models
# Create your models here.
class Author(models.Model):
    nid =models.AutoField(primary_key=True)
    name =models.CharField(max_length=32)
    age = models.IntegerField()
 #出版商模型
class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name =models.CharField(max_length=32)
    city = models.CharField(max_length=32)
#书籍
class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    # 与Publish建立一对多的关系,外键字段建立在多的一方
    publish = models.ForeignKey(to="Publish" ,to_field="nid",on_delete=models.CASCADE)
    #多对多关系
    authors = models.ManyToManyField(to="Author")
    def __str__(self):
        return self.title
