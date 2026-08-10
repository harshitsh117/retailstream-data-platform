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

# Download PostgreSQL JDBC driver
RUN wget -O /opt/spark/jars/postgresql-42.7.3.jar \
    https://jdbc.postgresql.org/download/postgresql-42.7.3.jar

WORKDIR /workspace

COPY deployment/spark/requirements.txt /tmp/requirements.txt

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

CMD ["/bin/bash"]