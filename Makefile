# Makefile for managing Jekyll project for BlackPythonDev

# Set up the environment by pulling the latest Ruby build definitions, installing Ruby 3.3.5,
# as seen in the .ruby-version file, installing required gems and Python packages,
# and configuring pre-commit hooks

.PHONY: setup-ruby setup-python install


install: setup-ruby setup-python

	# Install the necessary Ruby gems defined in the Gemfile
	- bundle install

	# Install Python dependencies defined in requirements-dev.txt
	- pip install -r requirements-dev.txt

	# Set up pre-commit hooks as defined in the configuration file
	- pre-commit install


setup-ruby:
	# Pull the latest ruby-build plugin updates
	- git -C /root/.rbenv/plugins/ruby-build pull

	# Install Ruby version 3.3.5 using rbenv
	- rbenv install 3.3.5

	# Set local version of ruby to 3.3.5
	- rbenv local 3.3.5


setup-python:
	# System Build Dependencies for pyenv
	- sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
		libbz2-dev libreadline-dev libsqlite3-dev wget curl libncurses5-dev \
		libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev

	# Install Pyenv
	- curl https://pyenv.run | bash

	# Add Pyenv to Environment
	@echo "Setting up pyenv in ~/.bash_profile, ~/.profile, and ~/.bashrc..."
	@if [ -f $$HOME/.bash_profile ]; then \
		echo "Appending to ~/.bash_profile"; \
		grep -qxF 'export PYENV_ROOT="$$HOME/.pyenv"' $$HOME/.bash_profile || echo 'export PYENV_ROOT="$$HOME/.pyenv"' >> $$HOME/.bash_profile; \
		grep -qxF '[[ -d $$PYENV_ROOT/bin ]] && export PATH="$$PYENV_ROOT/bin:$$PATH"' $$HOME/.bash_profile || echo '[[ -d $$PYENV_ROOT/bin ]] && export PATH="$$PYENV_ROOT/bin:$$PATH"' >> $$HOME/.bash_profile; \
		grep -qxF 'eval "$$(pyenv init -)"' $$HOME/.bash_profile || echo 'eval "$$(pyenv init -)"' >> $$HOME/.bash_profile; \
	else \
		echo "Appending to ~/.profile"; \
		grep -qxF 'export PYENV_ROOT="$$HOME/.pyenv"' $$HOME/.profile || echo 'export PYENV_ROOT="$$HOME/.pyenv"' >> $$HOME/.profile; \
		grep -qxF '[[ -d $$PYENV_ROOT/bin ]] && export PATH="$$PYENV_ROOT/bin:$$PATH"' $$HOME/.profile || echo '[[ -d $$PYENV_ROOT/bin ]] && export PATH="$$PYENV_ROOT/bin:$$PATH"' >> $$HOME/.profile; \
		grep -qxF 'eval "$$(pyenv init -)"' $$HOME/.profile || echo 'eval "$$(pyenv init -)"' >> $$HOME/.profile; \
	fi

	# Append to ~/.bashrc for interactive shells
	@echo "Appending to ~/.bashrc"
	@grep -qxF 'export PYENV_ROOT="$$HOME/.pyenv"' $$HOME/.bashrc || echo 'export PYENV_ROOT="$$HOME/.pyenv"' >> $$HOME/.bashrc
	@grep -qxF '[[ -d $$PYENV_ROOT/bin ]] && export PATH="$$PYENV_ROOT/bin:$$PATH"' $$HOME/.bashrc || echo '[[ -d $$PYENV_ROOT/bin ]] && export PATH="$$PYENV_ROOT/bin:$$PATH"' >> $$HOME/.bashrc
	@grep -qxF 'eval "$$(pyenv init -)"' $$HOME/.bashrc || echo 'eval "$$(pyenv init -)"' >> $$HOME/.bashrc

	@echo "Pyenv setup completed."

	# Install Python version
	- pyenv install 3.11.7

	# Set local python to 3.11.7
	- pyenv local 3.11.7


# Start the Jekyll development server
start:
	bundle exec jekyll serve


# Start the Jekyll server in detached mode (runs in the background)
start-detach:
	bundle exec jekyll serve --detach


# Stop the detached Jekyll server (Kill the background Jekyll process)
stop-detach:
	pkill -f jekyll
