FROM mcr.microsoft.com/vscode/devcontainers/base:bullseye AS base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

ENV PYTHONPATH="/workspace/src:$PYTHONPATH"

# The virtual environment is created in the working directory where rye is run
# so the development and production environments must be in the same directory respectively.
WORKDIR /workspace

RUN \
  --mount=type=cache,target=/var/lib/apt/lists \
  --mount=type=cache,target=/var/cache/apt/archives \
  apt-get update \
  && apt-get install -y --no-install-recommends build-essential

ENV RYE_HOME="/opt/rye"
ENV PATH="$RYE_HOME/shims:$PATH"

# RYE_INSTALL_OPTION is required to build.
# See: https://github.com/mitsuhiko/rye/issues/246
RUN curl -sSf https://rye-up.com/get | RYE_NO_AUTO_INSTALL=1 RYE_INSTALL_OPTION="--yes" bash

FROM base AS dev

RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
  --mount=type=bind,source=requirements.lock,target=requirements.lock \
  --mount=type=bind,source=requirements-dev.lock,target=requirements-dev.lock \
  --mount=type=bind,source=.python-version,target=.python-version \
  --mount=type=bind,source=README.md,target=README.md \
  rye sync --no-lock
RUN . .venv/bin/activate
RUN rye tools install pre-commit
RUN rye tools install cookiecutter

COPY . .
