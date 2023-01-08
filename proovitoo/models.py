from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.db.models import Model


class Header(models.Model):
    name = models.CharField(validators=[MinLengthValidator(3)], max_length=100)
    create_date = models.DateField('date created')
    reg_code = models.CharField(max_length=7, validators=[MinLengthValidator(7)], primary_key=True)
    search_string = models.CharField(max_length=500, null=True, blank=True)
    autofill_string = models.CharField(max_length=104, null=True, blank=True)

class Detail(models.Model):
    reg_code = models.ForeignKey(Header, on_delete=models.CASCADE)
    shareholder_first_name = models.CharField(max_length=100, null=True, blank=True)
    shareholder_last_name = models.CharField(max_length=100, null=True, blank=True)
    shareholder_company_name = models.CharField(max_length=100, null=True, blank=True)
    shareholder_company_reg_code = models.CharField(max_length=7, validators=[MinLengthValidator(7)], null=True, blank=True)
    capital = models.IntegerField(validators=[MinValueValidator(1)])
    id_code = models.CharField(max_length=11, validators=[MinLengthValidator(11)], null=True, blank=True)
    founder = models.BooleanField()
    physical_person = models.BooleanField()
    autofill_string = models.CharField(max_length=104, null=True, blank=True)

