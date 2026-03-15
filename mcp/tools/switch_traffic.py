import subprocess


def switch_to_region(region):

    print(f"[MCP] switching traffic to region: {region}")

    if region == "west":

        service = "demo-service-west"

    else:

        service = "demo-service-east"

    print(f"[MCP] routing traffic to {service}")

    # placeholder logic for now
    subprocess.run([
        "az",
        "containerapp",
        "show",
        "--name",
        service,
        "--resource-group",
        "overwatch-rg"
    ])

    print("[MCP] traffic switch executed")