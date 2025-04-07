from django.db import models

class Inspection(models.Model):
    Attribute_1 = models.CharField(max_length=50)
    Attribute_2 = models.CharField(max_length=50)
    Attribute_3 = models.CharField(max_length=50)
    Attribute_4 = models.CharField(max_length=50)
    Attribute_5 = models.CharField(max_length=50)
    Attribute_6 = models.CharField(max_length=50)
    Attribute_7 = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = "inspections_inspection"  # Unique table name for Inspection model in inspections app

class Condition(models.Model):
    Inspection = models.ForeignKey(
        Inspection,
        on_delete=models.CASCADE
    )
    Attribute_1 = models.CharField(max_length=50)
    Attribute_2 = models.CharField(max_length=50)
    Attribute_3 = models.CharField(max_length=50)
    Attribute_4 = models.CharField(max_length=50)
    Attribute_5 = models.CharField(max_length=50)
    Attribute_6 = models.CharField(max_length=50)
    Attribute_7 = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = "inspections_condition"  # Unique table name for Condition model in inspections app
