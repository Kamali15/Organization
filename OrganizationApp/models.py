from django.db import models

# Create your models here.

class Organization (models.Model):
    org_id = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created_at = models.DateField()
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class SubOrganization (models.Model):
    sub_org_id = models.CharField(primary_key=True,max_length=10)
    org = models.ForeignKey(Organization,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created_at = models.DateField()
    created_by = models.CharField(max_length=100)
    def __str__(self):
        return self.name +" "+ self.sub_org_id

class Division(models.Model):
    div_id = models.CharField(primary_key=True,max_length=10)
    sub_org = models.ForeignKey(SubOrganization,on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100)
    created_at = models.DateField()
    created_by = models.CharField(max_length=100)
    def __str__(self):
        return self.team_name
    

class SubDivision(models.Model):
    
    sub_div_id = models.CharField(primary_key=True,max_length=10)
    div = models.ForeignKey(Division,on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100)
    created_at = models.DateField()
    created_by = models.CharField(max_length=100)
    def __str__(self):
        return self.team_name

class Employee(models.Model):
    Emp_id = models.CharField(primary_key=True,max_length=10)
    sub_div = models.ForeignKey(SubDivision,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    job_title = models.CharField(max_length=100)
    def __str__(self):
        return self.name

