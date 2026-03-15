import subprocess


def deploy_container(service_name):

    print(f"[MCP] scaling container service {service_name}")

    cmd = [
        "az",
        "containerapp",
        "update",
        "--name",
        service_name,
        "--resource-group",
        "overwatch-rg",
        "--min-replicas",
        "2",
        "--max-replicas",
        "5"
    ]

    subprocess.run(cmd)

    print("[MCP] scaling operation completed")