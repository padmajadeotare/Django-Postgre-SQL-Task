from django.db import models


class Info(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    gender=models.CharField(max_length=10)
    email=models.EmailField()
    contact_no=models.TextField(blank=True)
    bio_description=models.TextField()
    id_proof=models.FileField(blank=True,null=True,upload_to="media/%Y/%m/%D")
    photo=models.ImageField(null=True,upload_to='media/')



    def __str__(self):
        return self.first_name
