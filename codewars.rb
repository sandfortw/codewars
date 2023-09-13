
def high(x)
  words = x.split(/\W+/)
  answer = ""
  high = 0
  words.each do |word|
    if value(word) > high
      require 'pry'; binding.pry
      answer = word
      high = value(word)
    end
  end
 answer
end


def value(word)
  word.chars.map do |char|
    char.ord - 96
  end.inject(:+)
end

p high(ARGV[0])