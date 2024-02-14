# BMI INDEX CALCULATOR
print("Welcome to the BMI Index Calculator.")
# Ask user for their height in meters.
height=input("What is your height in meters?\n")
# Type cast the height to a float.
height_float=float(height)
# Ask user for their weight in kilograms.
weight=input("What is your weight in kilograms?\n")
# Type cast the weight to a float.
weight_float=float(weight)
# BMI Index=weight(in kilograms)/height^2(in meters))
bmi_index=weight_float/(height_float**2)
print('Your BMI Index is '+
      str(bmi_index))
if(bmi_index<18.5):
  print("You are underweight.")
elif(18.5<bmi_index<25):
  print("You are normal weight.")
elif(25<bmi_index<30):
  print("You are slightly overweight.")
elif(30<bmi_index<35):
  print("You are obese.")
else:
  print("You are clinically obese.")