from django.db import models

class Stud(models.Model):
    stud_name = models.CharField(max_length=80)
    father_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    roll_number = models.BigIntegerField(unique=True)
    math = models.BigIntegerField()
    english = models.BigIntegerField()
    history = models.BigIntegerField()
    science = models.BigIntegerField()
    hindi = models.BigIntegerField()
    total = models.BigIntegerField(null=True, blank=True)
    percentage = models.FloatField(null=True, blank=True)
    result = models.CharField(max_length=20, null=True, blank=True)
    division = models.CharField(max_length=20, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate total marks
        self.total = self.math + self.english + self.history + self.science + self.hindi
        self.percentage=self.total/500*100
       
        count=0
        if self.math>=40:
            count+=1
        if self.english>=40:
            count+=1
        if self.history>=40:
            count+=1
        if self.hindi>=40:
            count+=1
        if self.science>=40:
            count+=1
        if count==5:
            self.result="Pass"
        elif count==4:
            self.result="Compartment"
        else:
            self.result="Fail"

        if self.result=="Pass":
            if self.percentage>=80:
                self.division="Distinction"
            if self.percentage>=60:
                self.division="First"
            if self.percentage>=45:
                self.division="Second"
            else:
                self.division="Third"
        else:
            self.division="NA"
   


        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return f"{self.stud_name} {self.roll_number}"

