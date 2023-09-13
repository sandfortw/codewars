# def alphanumeric?(string)
#   string.match?(/[[:alnum:]][[:blank:]]/)
# end


# Test.expect(!alphanumeric?(""))
# Test.expect(!alphanumeric?("hello world_"))
# Test.expect(alphanumeric?("HELLOworld123"))

#match letters and numbers and spaces, does not match anything

def order(words)
  words.split(' ').sort_by do |word|
    word.match(/[1-9]/).to_s.to_i
  end.join(' ')
end

order("is2 Thi1s T4est 3a") #=>"Thi1s is2 3a T4est"