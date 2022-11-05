# syntax=docker/dockerfile:1

FROM python:3.10-slim as python-base
ENV POETRY_HOME="/opt/poetry"
# create .venv in workdir
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
# no prompts from poetrry
ENV POETRY_NO_INTERACTION=1 
ENV APP_WORKDIR="/opt/api_server_mock"
ENV VENV_PATH="$APP_WORKDIR/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# `builder-base` stage is used to build deps + create our virtual environment
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for installing poetry
        curl \
        # deps for building python deps
        build-essential

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python3 -

# copy project requirement files here to ensure they will be cached.
WORKDIR $APP_WORKDIR
COPY poetry.lock pyproject.toml ./
COPY ./api_server_mock/ /api_server_mock/


# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-dev


# `development` image is used during development / testing
FROM python-base as development
ENV FASTAPI_ENV=development
WORKDIR $APP_WORKDIR
COPY api_server_mock $APP_WORKDIR/api_server_mock

# copy in our built poetry + venv
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $APP_WORKDIR $APP_WORKDIR

# quicker install as runtime deps are already installed
RUN poetry install

# will become mountpoint of our code
WORKDIR $APP_WORKDIR

EXPOSE 8080
CMD ["uvicorn", "--reload", "api_server_mock.main:app", "--port", "8080", "--host", "0.0.0.0"]


# `production` image used for runtime
FROM python-base as production
ENV FASTAPI_ENV=production
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
WORKDIR /api_server_mock
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]