# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"


def solution(input, markers)
  string = input
  markers.each do |marker|
    string = marker_strip(string, marker)
  end
  string.chop
end

def marker_strip(input, marker)
  array = []
  input.split("\n").each do |line|
    array << line.split(marker)
  end

  bing = array.map do |element|
    "#{element[0].strip}\n"
  end.join
end
solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])

# "apples, pears  grapes bananas "