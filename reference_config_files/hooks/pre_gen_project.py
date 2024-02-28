import subprocess
import sys
from subprocess import CalledProcessError

PROJECT_SLUG = "{{ cookiecutter.__project_slug }}"


def create_repo() -> bool:
    try:
        subprocess.run(
            [
                "gh",
                "repo",
                "create",
                f"The-Red-Line-Podcast/{PROJECT_SLUG}",
                "--private" if "{{ cookiecutter.private_repo }}" else "--public",
            ],
            capture_output=True,
            check=True,
        )
        print(f"Successfully created the {PROJECT_SLUG} repository.")
        return True
    except Exception:
        return False


def repo_already_exists() -> bool:
    try:
        existing_repos = subprocess.run(
            [
                "gh",
                "repo",
                "list",
                "The-Red-Line-Podcast",
                "--json",
                "name",
                "--jq",
                ".[].name",
            ],
            capture_output=True,
            check=True,
            encoding="utf-8",
        ).stdout

        if PROJECT_SLUG in existing_repos.strip().splitlines():
            return True
    except CalledProcessError:
        print("Failed to run command")
        sys.exit(1)
    else:
        return False


if __name__ == "__main__":
    if repo_already_exists():
        print(
            f"The repository {PROJECT_SLUG} already exists. Please use a different unique name."
        )
        sys.exit(1)

    # if not create_repo():
    #     sys.exit(1)
