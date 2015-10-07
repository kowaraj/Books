# -*- coding: utf-8 -*-
# Print the string “Hello, world.”
puts "[1] ========================="
puts "Hello, world!"

# For the string “Hello, Ruby,” find the index of the word “Ruby.”
puts "[2] ========================="
s = "Hello, Ruby"
s.index('Ruby')

# Print your name ten times.
puts "[3] ========================="
3.times { puts "Hello!" }

# Print the string “This is sentence number 1,” where the number 1 changes from 1 to 10.
puts "[4] ========================="
r = 1..4
r.each do |i| puts "This is sentence number %d" % i end

# Run a Ruby program from a file.
puts "[5] ========================="

# • Bonus problem: If you’re feeling the need for a little more, write a program that picks a random number. Let a player guess the number, telling the player whether the guess is too low or too high.
# (Hint: rand(10) will generate a random number from 0 to 9, and gets will read a string from the keyboard that you can translate to an integer.)


