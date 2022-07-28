# import the library
from unicodedata import name
from PyPDF2 import PdfFileReader, PdfFileWriter
import fitz
import os

list_file=os.listdir('./locxuan')

number=0
for file in list_file:
    # open the fitz file
    file='./locxuan'+'/'+file
    pdf = fitz.open(file)
    # select the page number
    
    # number of page
    page_num=pdf.page_count
    for i in range(page_num):
        page = pdf.loadPage(i)
        #get hinh chu nhat chua image
        a=page.get_images(full=True)


        for image in a:
            print(image)
            image_coor=page.get_image_rects(image)
            print(image_coor[0])
            
            # image_coor=page.get_image_bbox(image)
            page.set_cropbox((image_coor[0]))
            zoom = 2
            mat = fitz.Matrix(zoom, zoom)
            page_out=page.getPixmap(matrix = mat)
            
            out_put_name='./cau_kinh_thanh/'+str(number)+'.jpg'
            page_out.writePNG(out_put_name)
            number+=1
