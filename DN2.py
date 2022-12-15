import os
 
path_LFW = r'/home/faks/Downloads/openbr/data/LFW/img/'
# br -algorithm FaceRecognition -compare slika_1.jpg slika_2.jpg
br_ukaz = 'br -algorithm FaceRecognition -compare'
mera_podobnosti = open('mera_podobnosti.txt' ,'a')
ujemanje = open('oznake_ujemanje.txt','a')
with open('pairsDevTest.txt','r') as b:
	vrstice = b.readline()
	for i in range(int(vrstice)):
		line = b.readline().split()
		slika_1 = path_LFW + line[0] + '/' + line[0] + '_' + line[1].zfill(4) + '.jpg'
		slika_2 = path_LFW + line[0] + '/' + line[0] + '_' + line[2].zfill(4) + '.jpg'
		i = i + 1
	
		podobnost_v = os.popen(br_ukaz + ' ' + slika_1 + ' ' +  slika_2)
		podobnost = podobnost_v.read()
		podobnost_v.close()
		
		mera_podobnosti.write(podobnost)
		
		ujemanje.write('1\n') # ista oseba
	for j in range(int(vrstice)):
		line = b.readline().split()
		slika_1 = path_LFW + line[0] + '/' + line[0] + '_' + line[1].zfill(4) + '.jpg'
		slika_2 = path_LFW + line[2] + '/' + line[2] + '_' + line[3].zfill(4) + '.jpg'
		j = j + 1
		podobnost_v = os.popen(br_ukaz + ' ' + slika_1 + ' ' +  slika_2)
		podobnost = podobnost_v.read()
		podobnost_v.close()
		mera_podobnosti.write(podobnost)
		
		ujemanje.write('0\n') # razlicna oseba
		
mera_podobnosti.close()
ujemanje.close()
		
	
		
