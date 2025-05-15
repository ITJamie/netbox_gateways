from netbox.plugins import PluginTemplateExtension
from ipam.models import Prefix
from .models import Gateway
from ipaddress import IPv4Address


class IPGatewayTemplate(PluginTemplateExtension):
    models = ["ipam.ipaddress"]

    def left_page(self):
        return self.x_page()
        return ""

    def x_page(self):
        obj = self.context["object"]
        try:
            gateways_obj = Gateway.objects.get(gateway_ip=obj)
        except Gateway.DoesNotExist:
            gateways_obj = None
        if not gateways_obj:
            meow = 1
            related_prefixs = Prefix.objects.filter(
                vrf=obj.vrf,
                prefix__net_contains_or_equals=str(obj.address.ip),
                status="active",  # Only search for "active" prefixes
            ).prefetch_related("_site", "role")
            if len(related_prefixs) >= 1:
                try:
                    prefix = related_prefixs[
                        len(related_prefixs) - 1
                    ]  # get last prefix in the recordset above
                except Prefix.ValueError:
                    prefix = None
            else:
                prefix = None
        else:
            prefix = gateways_obj.prefix

        if not prefix:
            gateways_obj = None
        else:
            if not gateways_obj:
                try:
                    gateways_obj = Gateway.objects.get(prefix=prefix)
                except Gateway.DoesNotExist:
                    gateways_obj = None
        wildcard_bits = None
        if gateways_obj:
            try:
                prefix_subnet = str(gateways_obj.gateway_ip.address.netmask)
                wildcard_bits = str(
                    IPv4Address(int(IPv4Address(prefix_subnet)) ^ (2**32 - 1))
                )
            except:
                wildcard_bits = None

        return self.render(
            "netbox_gateways/ip_card.html",
            extra_context={
                "meow": "mix",
                "gateways_obj": gateways_obj,
                "prefix": prefix,
                "wildcard_bits": wildcard_bits,
            },
        )


class PrefixGatewayTemplate(PluginTemplateExtension):
    models = ["ipam.prefix"]

    def left_page(self):
        return self.x_page()
        return ""

    def x_page(self):
        obj = self.context["object"]
        try:
            gateways_obj = Gateway.objects.get(prefix=obj)
        except Gateway.DoesNotExist:
            gateways_obj = None
        wildcard_bits = None
        if gateways_obj:
            try:
                prefix_subnet = str(gateways_obj.gateway_ip.address.netmask)
                wildcard_bits = str(
                    IPv4Address(int(IPv4Address(prefix_subnet)) ^ (2**32 - 1))
                )
            except:
                wildcard_bits = None
        return self.render(
            "netbox_gateways/prefix_card.html",
            extra_context={
                "prefix": obj,
                "gateways_obj": gateways_obj,
                "wildcard_bits": wildcard_bits,
            },
        )


template_extensions = [IPGatewayTemplate, PrefixGatewayTemplate]
