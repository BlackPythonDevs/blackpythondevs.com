# Base image for Jekyll with Bullseye
FROM mcr.microsoft.com/devcontainers/jekyll:2-bullseye
LABEL org.opencontainers.image.source https://github.com/oleksis/blackpythondevs.com
LABEL org.opencontainers.image.description "Black Python Developers website with pre-installed dependencies."
ARG RUBY_VERSION=3.2.2

# Install essential tools, Python, pip, and Node.js
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y \
        build-essential \
        python3.11 \
        python3-pip \
        curl \
        nodejs \
    && python3 -m pip install --upgrade pip \
    && rm -rf /var/lib/apt/lists/*

# Set up Ruby environment and install Ruby $RUBY_VERSION
RUN echo 'eval "$(rbenv init -)"' >> ~/.bashrc \
    && /bin/bash -c 'source ~/.bashrc && rbenv install $RUBY_VERSION && rbenv global $RUBY_VERSION'

# Pre-install Python dependencies
COPY requirements-dev.txt /usr/local/requirements-dev.txt
RUN python3 -m pip install -r /usr/local/requirements-dev.txt

# Pre-install Ruby dependencies
COPY Gemfile Gemfile.lock /workspace/
RUN if [ -f /workspace/Gemfile ]; then bundle install; fi

# Install Playwright and its dependencies
RUN npx playwright install-deps && npx playwright install

# Copy the post-create script
COPY --chmod=0755 .github/.devcontainer/post-create-bpdevs.sh /usr/local/post-create-bpdevs.sh

# Cleanup to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Expose Jekyll server port
EXPOSE 4000/tcp
