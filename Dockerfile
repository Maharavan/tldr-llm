FROM python:3.11-slim

ARG USERNAME=appuser
ARG UID=1001
ARG GID=1001

RUN apt-get update && apt-get install -y \
build-essential \
&& rm -rf /var/lib/apt/lists/*

RUN groupadd --gid ${GID} ${USERNAME} \
&& useradd --uid ${UID} --gid ${GID} \
    --create-home --shell /bin/bash ${USERNAME}

WORKDIR /app


COPY requirements.txt .

RUN pip install --upgrade pip

RUN python -m pip install -r requirements.txt

COPY --chown=${UID}:${GID} . .


USER ${UID}:${GID}

EXPOSE 5000

CMD ["python","app.py","--host=0.0.0.0","--port=5000"]