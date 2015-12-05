import data
import math

def scale_vector(vr, scalar):
	new_vector = data.Vector((vr.x*scalar),(vr.y*scalar),(vr.z*scalar))
	return new_vector

def dot_vector(vr1, vr2):
	new_x = vr1.x * vr2.x 
	new_y = vr1.y * vr2.y
	new_z = vr1.z * vr2.z
	return new_x + new_y + new_z

def length_vector(vr):
	return math.sqrt(math.pow(vr.x,2)+math.pow(vr.y,2)+math.pow(vr.z,2))

def normalize_vector(vr):
	length = math.fabs(length_vector(vr))
	new_x = vr.x/length
	new_y = vr.y/length
	new_z = vr.z/length
	new_vector = data.Vector(new_x,new_y,new_z)
	return new_vector

def difference_point(pt1, pt2):
	new_x = pt1.x - pt2.x
	new_y = pt1.y - pt2.y
	new_z = pt1.z - pt2.z
	new_vector = data.Vector(new_x,new_y,new_z)
	return new_vector

def difference_vector(vr1, vr2):
	new_x = vr1.x - vr2.x
	new_y = vr1.y - vr2.y
	new_z = vr1.z - vr2.z
	new_vector = data.Vector(new_x,new_y,new_z)
	return new_vector

def translate_point(pt, vr):
	new_x = pt.x + vr.x 
	new_y = pt.y + vr.y
	new_z = pt.z + vr.z
	new_point = data.Point(new_x,new_y,new_z)
	return new_point

def vector_from_to(from_pt, to_pt):
	pt = difference_point(to_pt,from_pt)
	new_vector = data.Vector(pt.x,pt.y,pt.z)
	return new_vector