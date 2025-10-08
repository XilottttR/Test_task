FROM python:3.11-slim as base

ENV USER=to_do \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/core_task \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_VIRTUALENVS_IN_PROJECT=0

RUN apt-get update && apt-get install --no-install-recommends -y curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && addgroup --system $USER && adduser --system --group $USER

ENV BUILDER_DIR=/usr/core_task/$USER

FROM base as builder

WORKDIR $BUILDER_DIR

COPY pyproject.toml poetry.lock entrypoint.sh ./

FROM base

ENV HOME_DIR=/home/$USER \
    APP_DIR=/home/$USER/core_task

WORKDIR $APP_DIR

COPY --from=builder \
    $BUILDER_DIR/pyproject.toml \
    $BUILDER_DIR/poetry.lock \
    $BUILDER_DIR/entrypoint.sh \
    $HOME_DIR/

RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --with dev

COPY ./core_task $APP_DIR

ENV PYTHONPATH=$APP_DIR

RUN chown -R "$USER":"$USER" $APP_DIR && \
    chown -R "$USER":"$USER" /opt && \
    chmod +x $HOME_DIR/entrypoint.sh

RUN chown -R "$USER":"$USER" /home/"$USER"

USER $USER

ENTRYPOINT ["/home/to_do/entrypoint.sh"]

