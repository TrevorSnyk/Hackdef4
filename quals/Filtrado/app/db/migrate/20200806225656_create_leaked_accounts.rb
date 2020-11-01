class CreateLeakedAccounts < ActiveRecord::Migration[6.0]
  def change
  	create_table :accounts do |t|
  		t.string :email
  		t.string :password
  		t.string :leakedfrom
  		t.datetime :date
  	end
  end
end