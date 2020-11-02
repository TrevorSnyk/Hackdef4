FROM ruby:latest
LABEL maintainer="nogag@gmail.com"
WORKDIR /app/app

RUN   apt-get update && \
      apt-get install -y --no-install-recommends apt-utils cron python2 python-pip && \
      rm -rf /var/lib/apt/lists/*

# Install selenium 
RUN   pip install selenium==3.141.0

# Install latest-stable chrome browser all its dependencies
RUN   wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
      && echo "deb https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list \
      && apt-get update \
      && apt-get install -y google-chrome-stable unzip \
      && rm -rf /var/lib/apt/lists/* \
      && sed -i 's|HERE/chrome"|HERE/chrome" --disable-setuid-sandbox --no-sandbox|g' \
           "/opt/google/chrome/google-chrome"

# Install chromedriver.
RUN   export CHROMEDRIVER_RELEASE=$(curl --location --fail --retry 3 https://chromedriver.storage.googleapis.com/LATEST_RELEASE) \
      && curl --silent --show-error --location --fail --retry 3 --output /tmp/chromedriver_linux64.zip "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_RELEASE/chromedriver_linux64.zip" \
      && cd /tmp \
      && unzip chromedriver_linux64.zip \
      && rm -rf chromedriver_linux64.zip \
      && chmod +x chromedriver \
      && mv chromedriver /usr/local/bin/chromedriver

ADD     app/Gemfile       .
ADD     app/Gemfile.lock  .
RUN     bundle install

ADD     app/ .

EXPOSE  $PORT

RUN     bundle exec whenever --update-crontab

CMD     bundle exec rackup -p $PORT --host 0.0.0.0 config.ru