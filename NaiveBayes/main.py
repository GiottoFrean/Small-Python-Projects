import numpy as np

# Toy problem parameters:
true_W_probs = np.array([0.2,0.3,0.5])
true_T_means_given_W = np.array([22,15,17])
true_T_stds_given_W = np.array([4.2,3.4,3.9])
true_R_probs_given_W = np.array([[0.9,0,0.1],[0.1,0.1,0.7],[0,0.8,0.2],[0,0.1,0]])

# Settings for generating data:
number_of_data_points = 15

data = np.zeros((number_of_data_points,3))
print("Generating Data (up to 10 rows):")
for i in range(number_of_data_points):
	# Generate Data
	w_i = np.random.choice(np.arange(3),p=true_W_probs)
	t_i = np.random.normal(true_T_means_given_W[w_i],true_T_stds_given_W[w_i])
	r_i = np.random.choice(np.arange(4),p=true_R_probs_given_W[:,w_i])
	data[i,0]=w_i
	data[i,1]=t_i
	data[i,2]=r_i

	# Printout
	if(i<10):
		w_i_name = ["sun","rain","clear"][w_i]
		t_i_rounded = np.round(t_i,3)
		r_i_name = ["none", "few","lots","all"][r_i]
		print(str.format("weather: {:<10} temp: {:<10} raincoats: {:<10}", w_i_name,t_i_rounded,r_i_name))
