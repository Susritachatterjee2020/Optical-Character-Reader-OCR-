path ='UserForms'
myPicList = os.listdir(path)
print(myPicList)
print('Total Images {}'.format(len(myPicList)))
for j,y in enumerate(myPicList):
    img = cv2.imread(path+"/"+y)
kp2, des2 = orb.detectAndCompute(img, None)
imgKp2 = cv2.drawKeypoints(img,kp2,None)
