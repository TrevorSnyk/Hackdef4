require 'sinatra'
require 'sinatra/activerecord'
require 'sinatra/reloader'
require 'sinatra/base'

require_relative './models/account.rb'

RACK_ENV = 'development'

class HaveIBeenPwned < Sinatra::Base
	register Sinatra::ActiveRecordExtension
	get '/' do
		erb :index
	end

	post '/search' do
		@account = Account.where("email='#{params[:search]}'")[0]
		erb :results
	end

end