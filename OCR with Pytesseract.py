imgCrop= imgScan[r[0][1]:r[1][1],r[0][0]:r[1][0]]
if r[2] == 'text':
            print('{}: {}'.format(r[3],pytesseract.image_to_string(imgCrop)))
            myData.append(pytesseract.image_to_string(imgCrop))
