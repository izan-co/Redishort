# Use official Python 3.11 slim image.
FROM python:3.11-slim

WORKDIR /app

# Auto-accept Coqui TTS terms of service.
ENV COQUI_TOS_AGREED=1

# --- System Dependencies ---
# Install ffmpeg, imagemagick, and build tools.
RUN apt-get update && \
    apt-get install -y ffmpeg imagemagick dos2unix build-essential rustc pkg-config libsndfile1-dev curl unzip && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    # Fix ImageMagick security policy.
    echo "" > /etc/ImageMagick-7/policy.xml

# Install Deno (required by yt-dlp for JavaScript challenge solving)
RUN curl -fsSL https://deno.land/install.sh | sh
ENV DENO_INSTALL="/root/.deno"
ENV PATH="${DENO_INSTALL}/bin:${PATH}"

# Copy requirements first for caching.
COPY requirements.txt .

# Install PyTorch for CPU to save space.
RUN pip install torch==2.3.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cpu

# Install Python dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Install/Update yt-dlp with EJS components included
RUN pip install --upgrade "yt-dlp[default]"
