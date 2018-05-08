import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("test.csv", sep=";", header=None)
df.columns = ['x','y']
#print(df)

df_x = df.sort_values(['x','y'], ascending=[False, False])
df_y = df.sort_values(['y','x'], ascending=[False, False]) 
df_x = df_x.reset_index()
df_y = df_y.reset_index()

x_list = []
y_list = []

fig = plt.figure()
plt.scatter(df.x,df.y)
plt.grid()

df_x_prev = [-5555,-5555]
df_y_prev = [-5555,-5555]

x_axis_bool = True
y_axis_bool = True
for i,j in zip(range(len(df_x.index)), range(len(df_y.index))):
	'''FOR X-AXIS'''
	''' While Same X-axis has multiple same value, keep skipping'''
	if x_axis_bool == False and y_axis_bool==False:
		break
	if x_axis_bool:
		plt.pause(0.005)
		while df_x.x[i] == df_x_prev[0]:
			i+=1
			continue

		'''Condition to check axis '''
		#while len(x_list) > 0 and df_x.x[i] < df_x_prev[0] and 
		''' For first point case, where X-axis value is higher'''
		if df_x.x[i] > df_x_prev[0]:
			df_x_prev[0] = df_x.x[i]
			df_x_prev[1] = df_x.y[i]
			x_list.append((df_x.x[i], df_x.y[i]))

		elif df_x.y[i] > df_x_prev[1]:
			''' While next X-axis point has higher Y-value than current '''
			df_x_prev[0] = df_x.x[i]
			df_x_prev[1] = df_x.y[i]
			x_list.append((df_x.x[i], df_x.y[i]))
	
	if y_axis_bool:
		'''FOR Y-AXIS'''
		while df_y.y[j] == df_y_prev[1]:
			j+=1
			continue

		if df_y.y[j] > df_y_prev[1]:
			df_y_prev[0] = df_y.x[j]
			df_y_prev[1] = df_y.y[j]
			y_list.append((df_y.x[j], df_y.y[j]))

		elif df_y.x[j] > df_y_prev[0]:
			df_y_prev[0] = df_y.x[j]
			df_y_prev[1] = df_y.y[j]
			y_list.append((df_y.x[j], df_y.y[j]))
	if df_y.y[j] == x_list[-1][1]:
		y_axis_bool=False
	if df_x.x[i] == y_list[-1][0]:
		x_axis_bool=False

	plt.scatter(df_x.x[i], df_x.y[i], color='r')
	plt.scatter(df_y.x[j], df_y.y[j], color='g')

print(x_list)
print(y_list)
c_list = list(set(x_list).union(y_list))
print(c_list)


plt.show()
