from mcp.tools.restart_service import restart_service
from mcp.tools.switch_traffic import switch_to_region


class AzureMCPServer:

    def execute(self, action, data):

        if action == "restart_service":
            restart_service(data["service"])

        elif action == "switch_region":
            switch_to_region(data["region"])