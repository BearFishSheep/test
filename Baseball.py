"""
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#from sklearn.metrics import r2_score
#import statsmodels.api as sm
"""
'''
#将baseball.dat文件转换为baseball.csv文件
import pandas as pd
path0 = 'E:/Downloads/baseball0.dat'
data = pd.read_table(path0, header=0, sep=' ')
data = data.to_csv('E:/Downloads/baseball0.csv', index=False, header=True)
'''
"""
#导入csv数据
Data = pd.read_csv('E:/Downloads/baseball2.csv')

"""
'''
plt.figure(figsize=(16, 8))
plt.scatter(Data['obp'], Data['salary'], c='black')
plt.xlabel('obp')
plt.ylabel('salary')
plt.show()
'''
"""
X = Data.drop(['salary'], axis=1)
Y = Data['salary'].values.reshape(-1, 1)

#print(Y.shape[0])

for i in range(len(Y)):
	Y[i][0] = math.log(Y[i][0])
#print(Y)

reg = LinearRegression()
reg.fit(X, Y)
"""
'''
print("lnY = {:.5} + {:.5}*average + {:.5}*obp + {:.5}*runs + {:.5}*hits + {:.5}*doubles\
		+ {:.5}*triples + {:.5}*homeruns + {:.5}*rbis + {:.5}*walks + {:.5}*sos + {:.5}*sbs + {:.5}*errors\
		+ {:.5}*freeagent + {:.5}*arbitration + {:.5}*runsperso + {:.5}*hitsperso\
		+ {:.5}*hrsperso  + {:.5}*rbisperso  + {:.5}*walksperso  + {:.5}*obppererror\
		+ {:.5}*runspererror  + {:.5}*hitspererror  + {:.5}*hrspererror  + {:.5}*soserrors\
		+ {:.5}*sbsobp  + {:.5}*sbsruns".format(reg.intercept_[0], reg.coef_[0][0], reg.coef_[0][1], reg.coef_[0][2]\
			, reg.coef_[0][3], reg.coef_[0][4], reg.coef_[0][5], reg.coef_[0][6], reg.coef_[0][7], reg.coef_[0][8], reg.coef_[0][9], reg.coef_[0][10]\
				, reg.coef_[0][11], reg.coef_[0][12], reg.coef_[0][13], reg.coef_[0][14], reg.coef_[0][15], reg.coef_[0][16], reg.coef_[0][17]\
					, reg.coef_[0][18], reg.coef_[0][19], reg.coef_[0][20], reg.coef_[0][21], reg.coef_[0][22], reg.coef_[0][23], reg.coef_[0][24]\
						, reg.coef_[0][25]))


'''
'''
ls1 = []
for i in range(26):
	ls1.append(reg.coef_[0][i])


with open('E:/Downloads/baseball.txt', 'r') as f:
	data = f.readline()
	data = data.strip()
	ls2 = data.split()

	salary = 0
	for j in range(26):
		salary += ls1[j] * float(ls2[j])
	salary += reg.intercept_[0]
	print(math.exp(salary))
'''

