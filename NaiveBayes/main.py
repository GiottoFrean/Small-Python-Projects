import numpy as np

true_W_probs = np.array([0.2,0.3,0.5])
true_T_means_given_W = np.array([22,15,17])
true_T_stds_given_W = np.array([4.2,3.4,3.9])
true_R_probs_given_W = np.array([[0.9,0,0.1],[0.1,0.1,0.7],[0,0.8,0.2],[0,0.1,0]])

number_of_data_points = 250
test_ratio = 0.2

data = np.zeros((number_of_data_points,3))
print("Generating Data (printing up to 10 rows):")
for i in range(number_of_data_points):
	w_i = np.random.choice(np.arange(3),p=true_W_probs)
	t_i = np.random.normal(true_T_means_given_W[w_i],true_T_stds_given_W[w_i])
	r_i = np.random.choice(np.arange(4),p=true_R_probs_given_W[:,w_i])
	data[i,0]=w_i
	data[i,1]=t_i
	data[i,2]=r_i
	if(i<10):
		w_i_name = ["sun","rain","clear"][w_i]
		t_i_rounded = np.round(t_i,3)
		r_i_name = ["none", "few","lots","all"][r_i]
		print(str.format("weather: {:<10} temp: {:<10} raincoats: {:<10}", w_i_name,t_i_rounded,r_i_name))

number_of_test_items = int(number_of_data_points*test_ratio)
test_data = data[:number_of_test_items]
train_data = data[number_of_test_items:]
print("")
# Estimate the means, std of T|W:
# 1 fictional point is appended in the process (with value 0) to prevent errors if there is no data (e.g no sunny days) 
T_mean_conditioned_on_W = np.array([np.mean(np.append(train_data[train_data[:,0]==w,1],0)) for w in range(3)])
T_std_conditioned_on_W = np.array([np.std(np.append(train_data[train_data[:,0]==w,1],0)) for w in range(3)])
# Now calculate the categorical frequencies (raw W probabilities, and R|W)
W_frequencies = np.ones(3)
R_frequencies_given_W = np.ones((4,3))
for train_index in range(0,train_data.shape[0]):
	weather = int(train_data[train_index,0])
	raincoats = int(train_data[train_index,2])
	R_frequencies_given_W[raincoats,weather]+=1
	W_frequencies[int(weather)]+=1
R_probs_given_W = R_frequencies_given_W/np.sum(R_frequencies_given_W,axis=0)
W_prob = W_frequencies/np.sum(W_frequencies)
print(T_mean_conditioned_on_W.round(2), "  <- T mean|W")
print(T_std_conditioned_on_W.round(2), "  <- T std|W")
print(R_probs_given_W.round(2), "  <- prob R|W, rounded to 2dp")
print("")

def gaussian_pdf(x,mean,std): # needed to calculate probability density function for T in testing
	return (1/np.sqrt(2*np.pi*std**2))*np.exp(-0.5*((mean-x)/std)**2)

predicted_weather = np.zeros(number_of_test_items)
for test_index in range(0,test_data.shape[0]):
	temp = test_data[test_index,1]
	raincoats = int(test_data[test_index,2])
	weather_is_sunny_relative_likelihood = W_prob[0]*gaussian_pdf(temp,T_mean_conditioned_on_W[0],T_std_conditioned_on_W[0])*R_probs_given_W[raincoats,0]
	weather_is_rainy_relative_likelihood = W_prob[1]*gaussian_pdf(temp,T_mean_conditioned_on_W[1],T_std_conditioned_on_W[1])*R_probs_given_W[raincoats,1]
	weather_is_cloud_relative_likelihood = W_prob[2]*gaussian_pdf(temp,T_mean_conditioned_on_W[2],T_std_conditioned_on_W[2])*R_probs_given_W[raincoats,2]
	predicted_weather[test_index]=np.argmax([weather_is_sunny_relative_likelihood,weather_is_rainy_relative_likelihood,weather_is_cloud_relative_likelihood])
predicted_weather = predicted_weather.astype(int)
true_weather = test_data[:,0].astype(int)
print("total test accuracy:", np.mean((predicted_weather==true_weather)*100), "%")
print("accuracy on true sunny data:", np.mean((predicted_weather[true_weather==0]==true_weather[true_weather==0])*100), "%")
print("accuracy on true rainy data:", np.mean((predicted_weather[true_weather==1]==true_weather[true_weather==1])*100), "%")
print("accuracy on true cloudy data:", np.mean((predicted_weather[true_weather==2]==true_weather[true_weather==2])*100), "%")
