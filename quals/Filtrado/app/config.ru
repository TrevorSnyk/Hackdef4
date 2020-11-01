#!/usr/bin/env ruby
# frozen_string_literal: true

require 'rubygems'
require 'sinatra'
require 'sinatra/reloader'
require File.expand_path 'app.rb', __dir__

require './app'

configure do
  set :database, adapter: 'sqlite3', database: 'db/development.sqlite3'
end

run HaveIBeenPwned
