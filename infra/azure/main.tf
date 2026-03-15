terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.64"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "overwatch_rg" {
  name     = "overwatch-rg"
  location = var.primary_location
}

resource "azurerm_container_registry" "acr" {
  name                = var.acr_name
  resource_group_name = azurerm_resource_group.overwatch_rg.name
  location            = azurerm_resource_group.overwatch_rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "azurerm_log_analytics_workspace" "logs" {
  name                = "overwatch-logs"
  location            = azurerm_resource_group.overwatch_rg.location
  resource_group_name = azurerm_resource_group.overwatch_rg.name
  sku                 = "PerGB2018"
}

resource "azurerm_container_app_environment" "east_env" {
  name                       = "overwatch-east-env"
  location                   = var.primary_location
  resource_group_name        = azurerm_resource_group.overwatch_rg.name
  log_analytics_workspace_id = azurerm_log_analytics_workspace.logs.id
}

resource "azurerm_container_app_environment" "west_env" {
  name                       = "overwatch-west-env"
  location                   = var.backup_location
  resource_group_name        = azurerm_resource_group.overwatch_rg.name
  log_analytics_workspace_id = azurerm_log_analytics_workspace.logs.id
}