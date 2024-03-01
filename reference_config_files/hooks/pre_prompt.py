import subprocess
import sys


def is_docker_installed() -> bool:
    try:
        subprocess.run(["docker", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


def is_github_cli_installed() -> bool:
    try:
        subprocess.run(["gh", "--help"], capture_output=True, check=True)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    if not is_docker_installed():
        print("ERROR: Docker is not installed.")
        sys.exit(1)

    if not is_github_cli_installed():
        print("ERROR: github cli is not installed.")
        sys.exit(1)
