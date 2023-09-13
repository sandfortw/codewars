def max_sequence(arr)
  x = arr.length
  max_sum = 0
  require 'pry'; binding.pry
  until x == 0
    arr.each_cons(x) { |array| max_sum = array.sum if array.sum > max_sum }
    x -= 1
  end
  max_sum
end


p max_sequence([0, 1, 2, 3, -1, 2, 3]) #=>10