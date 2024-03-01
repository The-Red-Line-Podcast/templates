import subprocess
import sys


def is_docker_installed() -> bool:
    try:
        subprocess.run(["docker", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return (
            "./dockerenv"
            in subprocess.run(
                ["ls", "-la", "/.dockerenv"],
                capture_output=True,
                check=True,
                encoding="utf-8",
            ).stdout
        )


def is_github_cli_installed() -> bool:
    try:
        subprocess.run(["gh", "--help"], capture_output=True, check=True)
        return True
    except Exception:
        return False

# TODO function to check if ghcli is setup properly

if __name__ == "__main__":
    if not is_docker_installed():
        print("ERROR: Docker is not installed.")
        sys.exit(1)

    if not is_github_cli_installed():
        print("ERROR: github cli is not installed.")
        sys.exit(1)
