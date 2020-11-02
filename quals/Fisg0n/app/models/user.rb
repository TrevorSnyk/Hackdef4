class User < ActiveRecord::Base
  require 'base64'
  require 'digest'
  
  validates_presence_of :username
  validates_presence_of :password_digest
  validates :username, uniqueness: true

  def self.password_digest(username, password)
    Base64.encode64(Digest::SHA256.digest(username + password))
  end

  def self.delete_records
  	User.delete_all
    User.reset_pk_sequence
  end

  def self.check_password(username, password)
    user = User.where(username: username).first
    return false unless user

    user.password_digest == password_digest(username, password)
  end
end

