from django.db import models

# Create your models here.
class Veteran(models.Model):
    veteranID = models.AutoField(primary_key=True)
    veteranFirstName = models.CharField(max_length=255)
    #veteranMiddle_Name = models.CharField(max_length=255)
    veteranLastName = models.CharField(max_length=255)
    """
    Address = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    State = models.CharField(max_length=255)
    Zip = models.CharField(max_length=255)
    Phone_Num = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Birth_Place = models.
    Gender = models.CharField(ma)
    """

    def __str__(self):
        val = str(self.veteranID) + " "  + self.veteranFirstName + " "  + self.veteranLastName
        return val

class Interviewer(models.Model):
    interviewerID = models.AutoField(primary_key=True)
    interviewerFirstName = models.CharField(max_length=255)
    interviewerLastName = models.CharField(max_length=255)


    def __str__(self):
        val = str(self.interviewerID) + " "  + self.interviewerFirstName + " "  + self.interviewerLastName
        return val

class Audio(models.Model):
    audioID = models.AutoField(primary_key=True)
    audioTitle = models.CharField(max_length=255, default="No Title")
    audioLength = models.DurationField()

    def __str__(self):
        val = str(self.audioID) + " "  + str(self.audioTitle) + " " + str(self.audioLength)
        return val
    


class Interview(models.Model):
    interviewID = models.AutoField(primary_key=True)
    interviewDate = models.DateField()

    veteran = models.ForeignKey(Veteran, null=True, related_name='interviewers', on_delete=models.SET_NULL)
    interviewer = models.ForeignKey(Interviewer, null=True, related_name='interviewers', on_delete=models.SET_NULL, blank=True)
    audio = models.OneToOneField(Audio, null=True, related_name='interviewers', on_delete=models.SET_NULL, blank=True)


    def __str__(self):
        #print(self.veteran.veteranID,type(self.veteran.veteranID))
        #veteran_instance = Veteran.objects.get(veteranID=self.veteran)
        #interviewer_instance = Interviewer.objects.get(interviewerID=self.interviewer)
        val = str(self.interviewID) + " "  + str(self.interviewDate) + ", Veteran: "  + str(self.veteran.veteranFirstName) + " " + str(self.veteran.veteranLastName) + ", Interviewer : " + str(self.interviewer.interviewerFirstName) + " " + str(self.interviewer.interviewerLastName)
        #val = str(self.interviewID) + " "  + str(self.interviewDate)
        return val

    #veteran_ID = models.AutoField(primary_key=True)
    #veteran_FirstName = models.CharField(max_length=255)
    #veteran_LastName = models.IntegerField(default=0)



