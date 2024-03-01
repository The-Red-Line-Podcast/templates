# Project Templates

## Template Generation Prerequisites

- [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) recommended to install with [pipx](https://pipx.pypa.io/latest/installation/).
- [github cli](https://cli.github.com/)
  - github cli is setup with your credentials `gh auth login` or `gh auth refresh` if ssh key already setup
  - setup github cli to allow repo creation
  - setup github cli to allow repo deletion `gh auth refresh -h github.com -s delete_repo`
- [Optional] install [rye](https://rye-up.com/guide/installation/)

## Creating a New Project from Template

Run `cookiecutter https://github.com/The-Red-Line-Podcast/templates` and follow the prompts.


## Adding New Templates

### Template Development Prerequisites

- [docker](https://docs.docker.com/engine/install/)
- VScode `devcontainers` extension.

Any development should be done in the devcontainer!

### Creating a New Template

- Create a new directory with a clearly identifiable name
- Create the repository structure with all config files
- Template the repo according to [cookiecutter guide](https://cookiecutter.readthedocs.io/en/stable/)
- Copy the `hooks/`, `.pre-commit-config.yaml`, `Dockerfile`, `.devcontainer` and `pyproject.toml` from the reference_config_files
- Add the new template to the `cookiecutter.json` in the repo root

```json
{
    "templates": {
        "python-default": {
            "path": "./python-default",
            "title": "Python Default",
            "description": "Default Redline Podcast default template"
        },
        "new-template-name":{
            "path":"./path/to/new/template",
            "title":"Title of new template",
            "description":"Description of new template"
        }
    }
}

```

### Testing Template locally

Run `cookiecutter ./path/to/templates/repo`

## Roadmap

- Script that automatically copies reference config files to a new template directory
- Centralise hooks https://github.com/cookiecutter/cookiecutter/issues/1593
- Add cleanup logic for when project rendering fails
