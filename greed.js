// Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

//  Three 1's => 1000 points
//  Three 6's =>  600 points
//  Three 5's =>  500 points
//  Three 4's =>  400 points
//  Three 3's =>  300 points
//  Three 2's =>  200 points
//  One   1   =>  100 points
//  One   5   =>   50 point
// A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

// Example scoring

//  Throw       Score
//  ---------   ------------------
//  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
//  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
//  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
// In some languages, it is possible to mutate the input to the function. This is something that you should never do. If you mutate the input, you will not be able to pass all the tests.


function count(array, num){
  let counter = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] === num){
      counter++
    }
  }
  return counter
}


function score( dice ) {
  let score = 0;
  let board = {
                one: count(dice, 1),
                two: count(dice, 2),
                three: count(dice, 3),
                four: count(dice, 4),
                five: count(dice, 5),
                six: count(dice, 6)
              }
  if(board.one > 0){
    if(board.one >= 3){
      score += 1000
      board.one -= 3
    }
    while(board.one > 0){
      score += 100
      board.one -= 1
    }
  }
  if(board.five > 0){
    if(board.five >= 3){
      score += 500
      board.five -= 3
    }
    while(board.five > 0){
      score += 50
      board.five -= 1
    }
  }

  if(board.two >= 3){
    score += 200
  }
  if(board.three >= 3){
    score += 300
  }
  if (board.four >= 3){
    score += 400
  }
  if (board.six >= 3 ){
    score += 600
  }
  return score
}

console.log("Should be 1200:")
console.log(score( [1, 1, 1, 1, 1]))
console.log("Should be 500:")
console.log(score( [4, 4, 3, 4, 1]))
console.log("Should be 400:")
console.log(score( [3, 3, 3, 4, 1]))
console.log("Should be 300:")
console.log(score( [4, 3, 3, 4, 3]))
console.log("Should be 600:")
console.log(score([ 6, 6, 6, 3, 3 ]))