# from django.db import models
#
# class BaseAbstarctModel(models.Model):
#     created_at      =   models.DateTimeField(auto_now_add=True)
#     update_at       =   models.DateTimeField(auto_now=True)
#     deleted_at      =   models.DateTimeField(auto_now=True)
#
#
#     def soft_delete(self):
#         self.is_deleted=True
#         self.save()
#
#     class Meta:
#         abstract = True
#         ordering = ['-created_at']
