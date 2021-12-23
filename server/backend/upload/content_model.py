from django.db import models


class AddContent(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.IntegerField()
    title = models.CharField(max_length=50)
    faults = models.TextField()
    solution_one = models.TextField()
    solution_two = models.TextField()
    solution_three = models.TextField()
    uniqueCode = models.CharField(max_length=50)
    status_id = models.IntegerField()
    record_status = models.IntegerField()
    visibility = models.IntegerField()
    created_by = models.IntegerField()
    modified_by = models.IntegerField()
    date_created = models.DateField()
    time_created = models.TimeField()
    date_modified = models.DateField()
    time_modified = models.TimeField()

    class Meta:
        db_table = 'contents'

