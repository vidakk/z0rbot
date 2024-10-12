resource "azurerm_container_app_environment" "z0rbot-cae" {
  name = var.container_app_environment_name
  location = var.location
  resource_group_name = azurerm_resource_group.z0rbot-rg.name
}

resource "azurerm_container_app" "z0rbot-ca" {
    name = var.container_app_name
    container_app_environment_id = azurerm_container_app_environment.z0rbot-cae.id
    resource_group_name = azurerm_resource_group.z0rbot-rg.name
    revision_mode = "Single"

    identity {
      type = "SystemAssigned"
    }

    registry {
        server = "ghcr.io"
        username = "var.ghcr_username"
        password_secret_name = azurerm_key_vault_secret.github_token.name
    }

    template {
        container {
            name = "z0rbot"
            image = "ghcr.io/vidakk/z0rbot/z0rbot:latest"
            cpu = 0.25
            memory = "0.5Gi"

            env {
                name = "DISCORD_TOKEN"
                value = "var.discord_token"
            }
        }
    }
}