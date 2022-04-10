from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


gateways_buttons = [
    PluginMenuButton(
        link="plugins:netbox_gateways:gateway_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
        color=ButtonColorChoices.GREEN,
        permissions=["netbox_gateways.addedit_gateway"],
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_gateways:gateway_list",
        link_text="Gateway",
        buttons=gateways_buttons,
        permissions=["netbox_gateways.view_gateway"],
    ),
)
