from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class EmployeeDB(models.Model):
    employeeID = models.AutoField(primary_key=True)
    eName = models.CharField(max_length=255)
    eLastName = models.CharField(max_length=255, null = True)
    eMobNo = models.PositiveBigIntegerField()
    eEmail = models.CharField(max_length=255)
    eAddress = models.CharField(max_length=255)
    eGroup = models.CharField(max_length=255, null = True)
    eExtraInfo = models.CharField(max_length=255,null=True)
    eDateOfRenewable = models.DateField(null=True)