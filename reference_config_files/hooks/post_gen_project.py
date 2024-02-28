import subprocess
import sys

PROJECT_SLUG = "{{ cookiecutter.__project_slug }}"


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


def add_git_remote() -> bool:
    try:
        subprocess.run(
            [
                "git",
                "remote",
                "add",
                "origin",
                f"git@github.com:The-Red-Line-Podcast/{PROJECT_SLUG}.git",
            ],
            capture_output=True,
            check=True,
        )
        return True
    except Exception:
        return False


def push_initial_commit() -> bool:
    try:
        subprocess.run(
            [
                "git",
                "push",
                "--set-upstream",
                "origin",
            ],
            capture_output=True,
            check=True,
        )
        return True
    except Exception:
        return False


if __name__ == "__main__":
    if not init_git_repo():
        sys.exit(1)

    if not add_git_remote():
        sys.exit(1)

    # if not push_initial_commit():
    #     sys.exit(1)
