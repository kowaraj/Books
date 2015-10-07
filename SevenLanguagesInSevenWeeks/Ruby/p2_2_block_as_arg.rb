def my_call_block(&block)
  block.call
end

my_call_block {puts "passed_as_an_argument  - to my_call_block"}



