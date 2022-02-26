FROM python:3.7

ENV FLASK_APP=flask_server/flask_app.py

# Install system dependencies
RUN apt-get update \
    && apt-get -y install gcc make \
    && rm -rf /var/lib/apt/lists/*s

# Install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# Install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Copy all the necessary files
COPY . /app

# Upgrading pip and installing requirements
RUN pip install --no-cache-dir --upgrade pip
WORKDIR /app
RUN pip3 install --no-cache-dir -r resources/requirements.txt

# Running the application
CMD ["flask", "run", "--host", "0.0.0.0"]

EXPOSE 5000