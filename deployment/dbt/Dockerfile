FROM python:3.11-slim

WORKDIR /workspace

COPY deployment/dbt/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

CMD ["/bin/bash"]