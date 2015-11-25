$LOAD_PATH << "."

require 'd2_module.rb'
class A
  include ToFi
  attr_accessor :name

  def initialize(name)
    @name = name
  end

  def method_get_name_of_someclass
    'my name is = '+name+"\n"
  end
end
    
A.new('vasya').to_f
