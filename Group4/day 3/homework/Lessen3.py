# ცვლადებს მივანიჭეთ მნიშვნელობა
Name="mirian"
Surname="gelashvili"
Age=33
Next_Year=5

# დავპრინტეთ სახელი, გვრი, ასაკი, სტრინგის და ინტეგერის გაერთიანება (str) ორერატორით
print(Name+Surname)
print(Name+Surname+str(Age))

# დავპრინტეთ სახელი, გვარი, ასაკი, დაშორებით, (" ") ოპერატორის გამოყენებით
print(Name+" "+Surname)
print(Name+" "+Surname+ " " +str(Age))

# ასაკს დავუმატეთ ხუთი წელი
print(Name+Surname+str(Age+Next_Year))
print(Name+" "+Surname+ " " +str(Age+Next_Year))

# ყველა ცვალდი გავაერთიანეთ დაშორების გარეშე
print("I"+"am"+"is"+Name+Surname)
print("I"+" "+"am"+" "+"is"" "+(Name)+" "+(Surname))

# ყველა ცვლადი გავაერთიანეთ დაშორებით
print("I"+"am"+"is"+(Name)+(Surname)+"I"+"am"+str(Age)+"year"+"old")
print("I"+" "+"am"+" "+"is"+" "+(Name)+" "+(Surname)+" "+"I"" "+"am"" "+str(Age)+" "+"year"" "+"old")