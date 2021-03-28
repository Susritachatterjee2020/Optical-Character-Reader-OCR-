if r[2] == 'box':
    imgWarpGray = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2GRAY)  
    imgThresh = cv2.threshold(imgWarpGray, 170, 255, 
    cv2.THRESH_BINARY_INV)[1]  # APPLY THRESHOLD AND INVERSE
    totalPixels = cv2.countNonZero(imgThresh)
    if totalPixels>minThreshold:totalPixels=1
    else:totalPixels=0
    print(f'{r[3]}: {totalPixels}')
    myData.append(totalPixels)
cv2.putText(imgShow,str(myData[x]),(r[0][0], r[0][1]),
           cv2.FONT_HERSHEY_PLAIN,2.5,(0,0,255),4)
