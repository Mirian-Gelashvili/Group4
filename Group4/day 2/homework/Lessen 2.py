#შეიცავს რიცხვებს რომელიც აღნიშნავს ასაკს
age1=52
age2=55
age3=24

# შეიცავს სტრინგებს ""გამოყენებით, რომელიც შეიცავს არსებით სახელებს
mather ="mather"
father="father"
sister="sister"

# სტრინგისა და ინტეჯერის გაერთიანება Str ფუნქციით
print(mather+str(age1))
print(father+str(age2))
print(sister+str(age3))

# მნიშნელობებს შორის სიცარიელე
print(mather+" "+ str(age1)) 
print(father+" "+ str(age2))
print(sister+" "+ str(age3))

# ასაკს დამატებული 5
print(mather+" "+str(age1+5))
print(father+" "+str(age2+5))
print(sister+" "+str(age3+5))

# გრძელი სტრინგი
print("may"+(mather)+"is"+str(age1)+"year"+"old")
print("my"+(father)+"is"+str(age2)+"year"+"old")
print("may"+(sister)+"is"+str(age3)+"year"+"old")

# გრძელი სტრინგი სიცარიელეებით
print("my"" "+(mather)+" ""is"" "+str(age1)+" ""year"" "+"Old")
print("may"" "+(father)+" ""is"" "+str(age2)+" ""year"+" ""old")
print("may"" "+(sister)+" ""is"" "+str(age3)+" ""yera"+ " ""old")


