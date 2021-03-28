with open('DataOutput.csv','a+') as f:
        for data in myData:
            f.write(str(data)+',')
        f.write('n')
