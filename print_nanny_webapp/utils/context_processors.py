import djstripe.models
import djstripe.enums
from django.conf import settings


def settings_context(_request):
    """Settings available by default to the templates context."""
    # Note: we intentionally do NOT expose the entire settings
    # to prevent accidental leaking of sensitive information
    sold_out = (
        djstripe.models.Subscription.objects.filter(
            status=djstripe.enums.SubscriptionStatus.active
        ).count()
        >= settings.PAID_BETA_SUBSCRIPTION_LIMIT
    )
    return {
        "DEBUG": settings.DEBUG,
        "GOOGLE_ANALYTICS": settings.GOOGLE_ANALYTICS,
        "WS_BASE_URL": settings.WS_BASE_URL,
        "DISCORD_URL": settings.DISCORD_URL,
        "GITHUB_ISSUE_URL": settings.GITHUB_ISSUE_URL,
        "STRIPE_ENABLE_SUBSCRIPTIONS": settings.STRIPE_ENABLE_SUBSCRIPTIONS,
        "HELP_OCTOPRINT_PLUGIN_SETUP": settings.HELP_OCTOPRINT_PLUGIN_SETUP,
        "SOLD_OUT": sold_out,
    }
