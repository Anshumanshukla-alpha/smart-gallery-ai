# Generated manually for Smart Gallery AI.
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0004_event_photo_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyConsent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('policy_version', models.CharField(default='2026-11-01', max_length=32)),
                ('user', models.OneToOneField(on_delete=models.deletion.CASCADE, related_name='privacy_consent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
