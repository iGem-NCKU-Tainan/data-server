from django.db import models


class Data(models.Model):
    serialnum = models.FloatField()
    time = models.TextField()
    result = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.result
