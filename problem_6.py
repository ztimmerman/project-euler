#Sum square difference
#Calculate the sum of the squares of 1-100
#And the square of the sum of 1-100
#And add them togeher.

start_num=1
end_num=100

#Sum of the squares
sumOfSquares=sum([x*x for x in range(start_num,end_num+1)])

#Square of sum
squareofSum=sum([x for x in range(start_num,end_num+1)])
squareofSum*=squareofSum

print(squareofSum,'-',sumOfSquares,'=',squareofSum-sumOfSquares)