from django.db import models

# Create your models here.


class Group(models.Model):
    """
    model to display group
    """

    group_name = models.CharField(max_length=20, unique=True,)

    @classmethod
    def get_or_create(cls, name: str):
        try:
            group = cls.objects.get(group_name=name)
        except:
            group = cls.objects.create(group_name=name)

        return group

    def __str__(self):
        return self.group_name

class Chart(models.Model):
    """
    model to display chart
    """

    region = models.ForeignKey(Group)
    param = models.CharField(max_length=30)
    value = models.FloatField()

    def __str__(self):
         return '%s: %s'%(self.param, self.value)