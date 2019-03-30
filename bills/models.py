from django.db import models


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    operation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Bill(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    ident_category = models.ForeignKey('Category', models.DO_NOTHING, db_column='ident_category')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill'
        verbose_name_plural = 'Bills'
        ordering = ('date',)

    def __str__(self):
        return self.name

