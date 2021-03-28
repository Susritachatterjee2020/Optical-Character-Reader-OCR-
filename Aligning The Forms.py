srcPts = np.float32([kp2[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
dstPts = np.float32([kp1[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
M, _ = cv2.findHomography(srcPts, dstPts, cv2.RANSAC, 5.0)
h, w = imgQ.shape[:2]
imgScan = cv2.warpPerspective(img, M, (w, h))
imgShow = imgScan.copy()
imgMask = np.zeros_like(imgShow)
