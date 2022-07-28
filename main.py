import os
import numpy as np


if __name__ == '__main__':
    path='./cau_kinh_thanh'
    list_file=os.listdir(path)
    select_data=np.random.randint(low=1,high=len(list_file))
    open_file_name=path+'/'+str(select_data)+'.jpg'
    os.system('start'+open_file_name)