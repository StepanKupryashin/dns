from django.db import models
# Create your models here.
class Components(models.Model):
    type = models.TextField(blank=False, db_column="type", verbose_name="Тип комплектуещего", null=False)
    name = models.TextField(blank=False, db_column="name", verbose_name="Наиминование", null=False)
    price = models.IntegerField(blank=False, db_column="price",verbose_name="Цена")
    year = models.IntegerField(blank=False, db_column="year", verbose_name="Год выпуска")
    owner = models.TextField(blank=False, db_column="owner", verbose_name="Производитель")
    count = models.IntegerField(blank=False, db_column="count", verbose_name="количество")
    class Meta:
        verbose_name = "Компонент"
        verbose_name_plural = "Компоненты"
        



