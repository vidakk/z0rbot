resource "azurerm_resource_group" "z0rbot-rg" {
    name = var.resource_group_name
    location = var.location
}