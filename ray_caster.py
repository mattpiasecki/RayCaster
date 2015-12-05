import cast
import data
import sys
import commandline

read = commandline.reader(1) #read first file (input)
sphere_list = commandline.file_to_sphere_list(read)
eye_point = commandline.check_eye()
min_x,max_x,min_y,max_y,width,height = commandline.check_view()
light = commandline.check_light()
ambient = commandline.check_ambient()

cast.cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,ambient,light)


