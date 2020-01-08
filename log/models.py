from django.db import models

# Create your models here.


class ErrorLogger(models.Model):
    log_date = models.DateField(auto_now_add=True)
    log_time = models.TimeField(auto_now_add=True)
    error_type = models.CharField(max_length=300)
    error_msg = models.TextField()
    app = models.CharField(max_length=300, blank=True)
    url = models.URLField(blank=True)
    user_id = models.CharField(max_length=250, blank=True)

    # class Meta:
    #     db_table = 'error_logs'
