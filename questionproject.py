x = 0




print ("quiz time!")
print("(1) which of the following athletes are NOT sponsored by nike?")
print("1. Lebron James")
print("2. Michael Jordan")
print("3. Stephen Curry")
print("4. Derek Jeter")
athlete_answer = input("answer is number?: ")
if athlete_answer == "3" :
    print("Correct!")
else:
    print("incorrect")

right_answer = 0
if athlete_answer == "3":
    right_answer += 1

print("(2) what is 3(2-2)?")
answer = input("answer =")
if answer == "0" :
    print("correct!")
    
else:
    print("incorrect")
    
if answer == "0":
    right_answer += 1

print("(3)what shoe brand popularized the slogan ""The brand with the 3 stripes""? ")
print("1. nike")
print("2. adidas")
print("3. puma")
print("4. reebok")
answer_brand = input ("the brand is :")
if answer_brand == "2" :
    print("correct!")
    
else:
    print("incorrect")
    
if answer_brand == "2":
    right_answer += 1

print("(4) what model of adidas shoe was dubbed ""2015 shoe of the year"" by complex magazine? ")
print("1. adidas yeezy 350")
print("2. adidas tubular")
print("3. adidas x raf simons")
print("4. adidas ultra boost")
answer_shoe = input ("the shoe is :")
if answer_shoe == "4" :
    print("correct!")
    
else:
    print("incorrect")

if answer_shoe == "4":
    right_answer += 1

print ("(5) how many years has the Air Jordan brand been in business?")
answer = input (":")
if answer == "32":
    print("correct")
    
else:
    
    print("incorrect")

if answer == "32":
    right_answer += 1
        
total = right_answer / 5 * 100

print ("congratulations, you got", right_answer, "answer correct.")
print ("that is a score of" , total, "percent>")
        