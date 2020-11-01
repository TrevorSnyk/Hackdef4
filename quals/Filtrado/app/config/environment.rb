# frozen_string_literal: true

configure :development do
  set :database, 'sqlite3:db/haveibeenpwned.db'
end
