import xlsxwriter
import qrcode

img = qrcode.make('test text')
print(img)

img.save(r'C:\Users\Kishor Kore\Desktop\qrcode_test.png')

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook(r'C:\Users\Kishor Kore\Desktop\images.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 30)

# Insert an image.
worksheet.write('A2', 'Insert an image in a cell:')
worksheet.insert_image('B2', r'C:\Users\Kishor Kore\Desktop\qrcode_test.png')
 

workbook.close()
print("done")