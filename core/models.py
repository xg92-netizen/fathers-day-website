from django.db import models


class Enter(models.Model):
    username = models.CharField('用户名', max_length=150)
    phone = models.CharField('电话', max_length=11)

    class Meta:
        db_table = 'enter'
        verbose_name = '注册表单'
        verbose_name_plural = '注册表单'

    def __str__(self):
        return self.username
