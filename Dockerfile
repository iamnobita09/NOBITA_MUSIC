FROM python:3.10-slim-bullseye

# Step 1: Install Curl and GPG
RUN apt-get update && apt-get install -y curl gnupg2 ca-certificates && \
    # Step 2: Add Node.js 18.x (v15+ ki requirement puri karne ke liye)
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    # Step 3: Install all dependencies including latest Node.js and Git
    apt-get install -y --no-install-recommends \
    ffmpeg \
    aria2 \
    wkhtmltopdf \
    git \
    nodejs \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*



COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD bash start
