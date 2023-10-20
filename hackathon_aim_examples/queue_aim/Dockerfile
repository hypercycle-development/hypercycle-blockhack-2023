FROM python:3.8.17-slim-bullseye
LABEL GPUS=0 GPU_MEMORY=0

ENV DEBIAN_FRONTEND=1

WORKDIR /opt

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-pip \
    python3-dev \
    build-essential \
    cmake \
    git \
    curl \
    ffmpeg \
    ca-certificates \
    libjpeg-dev \
    libpng-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./app .

EXPOSE 4000

CMD ["python3", "./main.py"]
