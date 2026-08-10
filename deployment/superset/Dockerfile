FROM apache/superset:5.0.0

USER root

COPY deployment/superset/requirements.txt /tmp/requirements.txt

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt

USER superset