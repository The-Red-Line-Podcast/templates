import subprocess
import sys


def init_git_repo() -> bool:
    try:
        subprocess.run(["git", "init"], capture_output=True, check=True)
        subprocess.run(["git", "add", "."], capture_output=True, check=True)
        subprocess.run(
            ["git", "commit", "-m", "feat: initial commit"],
            capture_output=True,
            check=True,
        )
        return True
    except Exception:
        return False


if __name__ == "__main__":
    if not init_git_repo():
        sys.exit(1)

    print("Project successfully initialised")
