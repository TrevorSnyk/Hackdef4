require 'sinatra'
require 'sinatra/activerecord'
require 'sinatra/reloader'
require 'sinatra/base'
require 'activerecord-reset-pk-sequence'
include ERB::Util

require_relative './models/user.rb'

RACK_ENV = 'development'

register Sinatra::ActiveRecordExtension

class HackdefAcademy < Sinatra::Base

  get '/' do
  	@users = User.all.to_a
  	erb :index
  end

  post '/register' do
  	params.merge!(
        password_digest: User.password_digest(params[:username], params[:password])
      )
      user_params = params.delete_if { |k, _v| k == 'password' }
      puts user_params
      user = User.create!(user_params)
      redirect '/'
  end

  post '/login' do
      if User.check_password(params[:username], params[:password])
        @user = User.where(username: params[:username]).first
        erb :maintenance
      else
        redirect '/'
      end
  end
end
