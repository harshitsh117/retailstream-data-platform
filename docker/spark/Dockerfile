FROM apache/spark:3.5.6

USER root

RUN apt-get update && \
    apt-get install -y \
        python3-pip \
        git \
        curl \
        wget \
        unzip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY docker/spark/requirements.txt /tmp/requirements.txt

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

CMD ["/bin/bash"]