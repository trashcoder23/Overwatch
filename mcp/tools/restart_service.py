import subprocess


def restart_service(service_name):

    print(f"[MCP] restarting container app {service_name}")

    cmd = [
        "az",
        "containerapp",
        "revision",
        "restart",
        "--name",
        service_name,
        "--resource-group",
        "overwatch-rg"
    ]

    subprocess.run(cmd)

    print("[MCP] restart triggered")