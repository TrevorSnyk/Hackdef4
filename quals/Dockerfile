FROM ruby:latest

WORKDIR /app/app

ADD     app/Gemfile       .
ADD     app/Gemfile.lock  .
RUN     bundle install

ADD     app/ .

EXPOSE  $PORT

CMD     bundle exec rackup -p $PORT --host 0.0.0.0 config.ru