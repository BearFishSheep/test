import math
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
	ls = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
	sum = 0
	for i in ls:
		sum += i**2
	t = int(math.sqrt(sum)/2)
	return t
print(predict_age(65,60,75,55,60,63,64,45))