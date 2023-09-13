

# def cakes(recipe, available)
#   array = []
#   available.each do |aname, aamount|
#    recipe.each do |rname, ramount|
#     require 'pry'; binding.pry
#     array << (aamount / ramount)
#    end
#   end
#   array.min
# end

def cakes(recipe, available)
  array = []
  recipe.each do |ingredient, amount|
    if available[ingredient].nil?
      array << 0
    else
      array << (available[ingredient] / recipe[ingredient])
    end
  end
  array.min
end

p cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200}); 
#=>2