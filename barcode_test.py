from object_data import data

while True:
    barcode_data = input("바코드를 찍어주세요 : ")
    print("바코드정보 = " + barcode_data)

    if barcode_data in data.keys():
        print(data[barcode_data])
 
    else:
        continue

    if data == 'q':
        break