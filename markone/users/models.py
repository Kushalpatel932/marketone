from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime
from pytz import timezone,UTC
from django.utils.translation import gettext_noop

class UserProfile(models.Model):

    GENDER_CHOICES = (
        ('m', gettext_noop('Male')),
        ('f',gettext_noop('Female')),
        ('o',gettext_noop('Other/Prefer Not to Say'))
    )

    user = models.OneToOneField(User,unique=True,related_name="profile",on_delete=models.CASCADE,db_index=True)
    full_name =models.CharField(max_length=500,null=True,blank=True,db_index=True)
    year_of_birth = models.IntegerField(blank=True,null=True,db_index=True)
    gender = models.CharField(blank=True,null=True,max_length=6, db_index=True,choices=GENDER_CHOICES)


    """  
        property method update
        property to set and get delet value attribute 
        age work like attribute in call   
    """
    @property
    def age(self):
        year_of_birth = self.year_of_birth
        year = datetime.now(UTC).year
        if year_of_birth is not None:
            return self._calculate_age(year,year_of_birth)
    
    def _calculate_age(self,year,year_of_birth):
        return year - year_of_birth
    