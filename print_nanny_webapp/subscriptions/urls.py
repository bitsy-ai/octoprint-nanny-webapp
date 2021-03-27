from django.urls import include, path

from print_nanny_webapp.subscriptions.views import SubscriptionsListView, subscriptions_payment_view_create

app_name = "subscriptions"

urlpatterns = [
    path(r"^stripe/", include("djstripe.urls", namespace="djstripe")),
    path("", SubscriptionsListView.as_view(), name="list"),
    path("payment", subscriptions_payment_view_create, name="payment"),
]
