from extras.plugins import PluginConfig


class NetBoxGatewayConfig(PluginConfig):
    name = "netbox_gateways"
    verbose_name = " Netbox Gateway"
    description = "Manage simple prefix default gateways"
    version = "0.2"
    base_url = "nb_gateways"


config = NetBoxGatewayConfig
