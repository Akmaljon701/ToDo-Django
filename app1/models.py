from django.db import models

class Kundalik(models.Model):
    vaqt = models.CharField(max_length=100)
    malumot = models.TextField()
    holat = models.CharField(max_length=100, choices=(
        ('Boshlandi', 'Boshlandi'),
        ('Bajarilmoqda', 'Bajarilmoqda'),
        ('Bajarildi', 'Bajarildi')
    ))

    def __str__(self):
        return f"{self.vaqt} - {self.holat}"