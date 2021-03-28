path ='UserForms'
myPicList = os.listdir(path)
print(myPicList)
print('Total Images {}'.format(len(myPicList)))
for j,y in enumerate(myPicList):
    img = cv2.imread(path+"/"+y)
kp2, des2 = orb.detectAndCompute(img, None)
imgKp2 = cv2.drawKeypoints(img,kp2,None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
matches = bf.match(des2, des1)
matches.sort(key = lambda x: x.distance)
good = matches[:int(len(matches)*(per/100))]
imgMatches = cv2.drawMatches(img, kp2, imgQ, kp1, good,None, flags=2)
