from skimage.feature import hog
import numpy as np
import matplotlib.image as img 






path_LFW_A = r'C:\Users\cr008\OneDrive\Desktop\lfwa\lfw2\lfw2' + '\\'

slike_pairs = []
def slike(dokument):
	with open(dokument,'r') as b:
		vrstice = b.readline()
		
		for i in range(int(vrstice)):
			line = b.readline().split()
			
			slika_1 = path_LFW_A +  line[0] + '\\' + line[0] + '_' + line[1].zfill(4) + '.jpg'
			slika_2 = path_LFW_A +  line[0] + '\\' + line[0] + '_' + line[2].zfill(4) + '.jpg'
			i = i + 1
			slike_pairs.append([slika_1, slika_2])
		for j in range(int(vrstice)):
			line = b.readline().split()
			slika_1 = path_LFW_A + line[0] + '\\' +  line[0] + '_' + line[1].zfill(4) + '.jpg'
			slika_2 = path_LFW_A + line[2] +  '\\' +  line[2] + '_' + line[3].zfill(4) + '.jpg'
			j = j + 1
			slike_pairs.append([slika_1,slika_2])
		
	return slike_pairs

test = slike('pairsDevTest.txt')


# hog deskriptorje

fd_train = []

for  pair in test:
		image1 = img.imread(pair[0])
		image2 = img.imread(pair[1])
		slika1 = (image1[50:200,50:180])
		slika2 = (image2[50:200,50:180])
	
		
		

		
		fd1, hog_image_1 = hog(slika1, orientations=12,pixels_per_cell=(8,8),cells_per_block=(2,2), block_norm = 'L2-Hys',visualize=True)
		fd2, hog_image_2 = hog(slika2, orientations=12,pixels_per_cell=(8,8),cells_per_block=(2,2),block_norm = 'L2-Hys',visualize=True)
		

		fd = np.concatenate((fd1, fd2))
		fd_train.append(fd)
		
		

		np.save('hog_test_L2_Hys', fd_train)



	





	