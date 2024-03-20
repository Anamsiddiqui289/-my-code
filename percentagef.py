# percentage= given marks*100/totalmarks

student_name=str(input("tell me your name please "))


#sir is 2nd input pe jub mene double aurgument use kya isny error diya 
# but f string function boht wonderful he
students_marks=int(input(f"enter your exam marks  {student_name}"))

totalmarks=450

percentage = students_marks*100//totalmarks

print(f"your percentage is  {percentage}   %")