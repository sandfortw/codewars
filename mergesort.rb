p [1, 4, 2, 5, 3, 6].sort
def merged(first, second)
  first.zip(second).flatten
end



merged([1,2,3],[4,5,6]) #=> [1,2,3,4,5, 6]
