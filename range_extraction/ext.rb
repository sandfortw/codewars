

def solution(list)
  range_array = []
  list.each_with_index do |num, index|
    if (num - 1 == list[index - 1] && num - 2 == list[index - 2]) || (num + 1 == list[index + 1] && num - 1 == list[index - 1])
      nil
    elsif num + 1 == list[index + 1] && num + 2 == list[index + 2]
      last_number = 0
      new_num = num
      until new_num + 1 != list[index + 1]
        last_number = list[index + 1] if list[index + 1]
        new_num += 1
        index += 1
      end
      range_array << "#{num}-#{last_number}"
    else
      range_array << num.to_s
    end
  end
  range_array.join(',')
end
