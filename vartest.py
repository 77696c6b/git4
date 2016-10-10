#There is 17 terms to test for suitability for variable. each term was assigned value=1 . run cycle through utlil idle returned error.



apple = 1
APPLE = 1
Apple2 = 1  
#1Apple = 1                        <---first error var name can not start with a number
#account number = 1  <---second error no spaces allowed
account_number  = 1
#account.number = 1  <--- third error 
accountNumber = 1 
fred = 1 
Fred = 1
Return = 1
return_value = 1 
#5Return = 1  <---forth error again no numbers as first characker.
GreatBigVariable = 1 
greatBigVariable = 1 
great_big_variable = 1 
#great.big.variable = 1   <---fifth error


print (apple+APPLE+Apple2+account_number +accountNumber+ fred +Fred + Return + return_value +GreatBigVariable +greatBigVariable + great_big_variable  )



"""
#out of  17 terms to test following 5 terms were found illegal:

1Apple                      <---first error var name can not start with a number
account number  <---second error no spaces allowed
account.number <--- third error 
5Return = 1  <---forth error again no numbers as first characker.
great.big.variable = 1   <---fifth error



program returns 12 
"""
input()