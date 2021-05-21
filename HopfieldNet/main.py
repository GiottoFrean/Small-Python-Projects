import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def save_img(img,name):
	fig = go.Figure()
	fig.add_trace(go.Image(z=img.reshape(img.shape[0],img.shape[1],1).repeat(3,axis=2)*255))
	fig.update_xaxes(showticklabels=False).update_yaxes(showticklabels=False)
	fig.update_layout(margin=dict(t=0,l=0,b=0,r=0))
	fig.update_layout(paper_bgcolor="darkred",plot_bgcolor="darkred")
	fig.update_layout(font=dict(family="Times",size=18))
	fig.write_image(name,width=10*img.shape[1],height=10*img.shape[0])

def make_some_image(rows,cols):
	center_row = np.random.randint(int(rows/4),int(3*rows/4))+0.5
	center_col = np.random.randint(int(cols/4),int(3*cols/4))+0.5
	center = np.array([center_row,center_col])
	pixel_positions = np.mgrid[:rows,:cols].reshape(2,-1).T
	dif = pixel_positions-center
	vecs = np.random.normal(0,1,(3,2))
	cos_angles = dif.dot(vecs.T)/np.outer(np.sqrt(np.sum(dif**2,axis=1)),np.sqrt(np.sum(vecs**2,axis=1)))
	anglular_dif = np.arccos(cos_angles)
	min_ang_dif = np.argmin(cos_angles,axis=1)
	img = ((min_ang_dif.reshape(rows,cols)/vecs.shape[0])<0.5)*1
	return img

image_size = 16
flipped_pixels = int(0.1*image_size**2)

print("making training images")
images = np.array([make_some_image(image_size,image_size) for i in range(5000)])

print("making covariance")
imaged_2d = images.reshape(images.shape[0],-1)
images_2d_normalized = imaged_2d*2-1
covariance = images_2d_normalized.T.dot(images_2d_normalized)
normalized_covariance = covariance/images_2d_normalized.shape[0]

print("making fake images")
test_images = np.array([make_some_image(image_size,image_size) for i in range(15)])

print("saving example images")
for n in range(test_images.shape[0]):
	test_img = test_images[n]
	save_img(test_img,"test_img"+str(n)+".jpg")
	cut_img = test_img
	flipped_row_vec = np.random.randint(0,test_img.shape[0],flipped_pixels)
	flipped_col_vec = np.random.randint(0,test_img.shape[0],flipped_pixels)
	cut_img[flipped_row_vec,flipped_col_vec]=1-cut_img[flipped_row_vec,flipped_col_vec]
	save_img(cut_img,"test_img"+str(n)+"_cut.jpg")
	weighted_sum = (cut_img.reshape(-1)*2-1).dot(normalized_covariance)
	reproducted_img = 1/(1+np.exp(-weighted_sum)).reshape(image_size,image_size)
	img_rounded = reproducted_img.round(0).astype(int)
	save_img(img_rounded,"test_img"+str(n)+"repro.jpg")





