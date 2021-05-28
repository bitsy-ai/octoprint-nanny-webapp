from django.db import migrations

def assign_beta_tester(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    User = apps.get_model("users", "User")
    MemberBadge = apps.get_model("subscriptions", "F")

    for user in User.objects.all():
        member_badge = MemberBadge(type="BETA_TESTER", user = user)
        member_badge.save()

class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(assign_beta_tester),
    ]