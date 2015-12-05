from data import *
from vector_math import *
import math

def sphere_intersection_point(ray,sphere):
	A = dot_vector(ray.dir,ray.dir)
	B = dot_vector(scale_vector(difference_point(ray.pt,sphere.center),2),ray.dir)
	C = dot_vector(difference_point(ray.pt,sphere.center),difference_point(ray.pt,sphere.center)) - math.pow(sphere.radius,2)
	if (math.pow(B,2) - 4*A*C) >=0:
		t = (-B + (math.sqrt(math.pow(B,2) - (4*A*C)))) / (2*A)
		t2 = (-B - (math.sqrt(math.pow(B,2) - (4*A*C)))) / (2*A)
		if (t > 0) and (t2 > 0):
			if (t < t2):
				return translate_point(ray.pt,scale_vector(ray.dir,t))
			else :
				return translate_point(ray.pt,scale_vector(ray.dir,t2))
		elif t>0:
			return translate_point(ray.pt,scale_vector(ray.dir,t))
		elif t2>0:
			return translate_point(ray.pt,scale_vector(ray.dir,t2))
		else :
			return None
	else :
		return None

def find_intersection_points(sphere_list,ray):
	return [(x,sphere_intersection_point(ray,x)) for x in sphere_list if sphere_intersection_point(ray,x)]
		
def sphere_normal_at_point(sphere,point):
	return normalize_vector(vector_from_to(sphere.center,point))
