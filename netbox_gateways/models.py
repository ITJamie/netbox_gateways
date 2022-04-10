from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet


class Gateway(NetBoxModel):
    # vrf is used mainly for filtering prefix and ips.
    vrf = models.ForeignKey(
        to="ipam.vrf",
        on_delete=models.PROTECT,
        # related_name='+',
        blank=True,
        null=True,
        related_name="+",
    )
    prefix = models.OneToOneField(
        to="ipam.Prefix",
        on_delete=models.CASCADE,
        # related_name='+',
        blank=True,
        null=True,
        related_name="gateway",
        unique=True,
    )
    gateway_ip = models.OneToOneField(
        to="ipam.IPAddress",
        on_delete=models.CASCADE,
        # related_name='+',
        blank=True,
        null=True,
        related_name="gateway",
    )

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return str(f"#{self.id}")

    def get_absolute_url(self):
        return reverse("plugins:netbox_gateways:gateway", args=[self.pk])
