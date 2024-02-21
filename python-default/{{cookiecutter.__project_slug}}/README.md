# Project

{{cookiecutter.description}}

## Project Setup

This repository uses cross platform devcontainers+docker to manage project dependencies
and project setup.

### Prerequisites

- [Docker](https://docs.docker.com/engine/install/)
- VScode `devcontainers` extension.

#### VScode (Recommended)

Attach the devcontainer using the VScode extension ...WIP

See more here [https://containers.dev/supporting.html](https://containers.dev/supporting.html)

## Usage

### Basic Commands

All rye commands can be found here [rye-commands](https://rye-up.com/guide/commands/)
Commonly used:

- `rye add <package>`
- `rye remove <package>`
- `rye format`, uses built in ruff
- `rye lint`, uses built in ruff

### Commit Messages

All commit message must follow the conventional commit standard [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).
There is a pre-commit hook using commitizen checking the commit message against this standard.

## Documentation

Add documentation on how to run this project here.
