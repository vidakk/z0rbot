variable "resource_group_name" {
    default = "rg-z0rbot-westeurope-001"
}

variable "location" {
    default = "westeurope"
}

variable "container_app_environment_name" {
    default = "cae-z0rbot-westeurope-001"
}

variable "discord_token" {
    type = string
    sensitive = true
}