output "resource_group_name" {
  value = azurerm_resource_group.overwatch_rg.name
}

output "acr_login_server" {
  value = azurerm_container_registry.acr.login_server
}

output "east_container_environment" {
  value = azurerm_container_app_environment.east_env.name
}

output "west_container_environment" {
  value = azurerm_container_app_environment.west_env.name
}