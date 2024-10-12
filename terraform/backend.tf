terraform{
    required_version = "1.9.7"
    required_providers {
        azurerm = {
            source = "hashicorp/azurerm"
            version = "4.5.0"
        }
    }
    backend "azurerm" {
        resource_group_name = "rg-terraform-github-actions-state"
        storage_account_name = "z0rbottfstate" #change this
        container_name = "tfstate"
        key = "terraform.tfstate"
        use_oidc = true
    }
}