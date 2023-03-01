def score(dice):
    points = 0
    counts = [0] * 7 # We only care about 1-6 dice rolls, so we'll create a list of length 7 to ignore the 0th index.
    
    # Count the number of times each dice roll appears
    for roll in dice:
        counts[roll] += 1
    
    # Calculate the points earned based on the counts
    for i in range(1, 7):
        if counts[i] >= 3:
            if i == 1:
                points += 1000
            else:
                points += i * 100
            counts[i] -= 3
            
        if i == 1:
            points += counts[i] * 100
        elif i == 5:
            points += counts[i] * 50
    
    return points
  
  
  from solution import score
import codewars_test as test

@test.describe("Example Tests")
def example_tests():
    
    @test.it("Example cases")
    def example_cases():
        test.assert_equals( score( [5, 1, 3, 4, 1] ),  250)
        test.assert_equals( score( [1, 1, 1, 3, 1] ), 1100)
        test.assert_equals( score( [2, 3, 4, 6, 2] ),    0)
        test.assert_equals( score( [4, 4, 4, 3, 3] ),  400)
        test.assert_equals( score( [2, 4, 4, 5, 4] ),  450)
