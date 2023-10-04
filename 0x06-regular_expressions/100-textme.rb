#!/usr/bin/env ruby

# Extract information from the input string using regex
matches = ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

# Initialize arrays to store extracted data
from_values = []
to_values = []
flags_values = []

# Loop through the matches and extract values
matches.each do |match|
  from_values << match[0]
  to_values << match[1]
  flags_values << match[2]
end

# Join the extracted values with commas and print
puts "From: #{from_values.join(", ")}"
puts "To: #{to_values.join(", ")}"
puts "Flags: #{flags_values.join(", ")}"
