from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_admin_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    user, _ = User.objects.get_or_create(
        username='gaoxiaoya',
        defaults={
            'email': '1737486800@qq.com',
            'first_name': 'wqok',
            'is_staff': True,
            'is_superuser': True,
            'is_active': True,
        },
    )
    user.email = '1737486800@qq.com'
    user.first_name = 'wqok'
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.password = make_password('gxy20081006')
    user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0002_alter_enter_options'),
    ]

    operations = [
        migrations.RunPython(create_admin_user, migrations.RunPython.noop),
    ]
