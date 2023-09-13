array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] #=>[1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
#got                                      [1, 8, 2, 6, 3, 4, 4, 2, 5, 0]

def sort_array(source_array)
  odds = source_array.select{ |num| num.odd? }.sort
  source_array.map { |num| num.odd? ? odds.shift : num }
end

p sort_array(array)