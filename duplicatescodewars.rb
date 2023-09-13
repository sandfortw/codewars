def duplicate_count(text)
  x = text.downcase.chars.tally do |char|
    char
  end
  require 'pry'; binding.pry
 y = x.count do |k , v|
    v > 1
  end
  y
end


# print duplicate_count("") #0)
# print duplicate_count("abcde") #, 0)
# print duplicate_count("abcdeaa") #, 1)
print duplicate_count("abcdeaB")# , 2)
# print duplicate_count("Indivisibilities") #, 2)