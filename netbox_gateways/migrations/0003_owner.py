import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0015_owner'),
        ('netbox_gateways', '0002_custom_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='gateway',
            name='owner',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.owner'
            ),
        ),
    ]
