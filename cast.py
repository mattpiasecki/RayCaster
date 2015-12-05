import collisions
import data
import vector_math
import math
import data
import vector_math

def comp(sphere_list,inter,light,sphere,int,eye_point):
	n = collisions.sphere_normal_at_point(sphere,int)
	scaled_normal = vector_math.scale_vector(n,.01)
	Pe = vector_math.translate_point(inter[0][1],scaled_normal)
	vr_light = vector_math.vector_from_to(Pe,light.pt)
	L_dir = vector_math.normalize_vector(vr_light)
	dot_product = vector_math.dot_vector(n,L_dir)
	reflection_vr = vector_math.difference_vector(L_dir,vector_math.scale_vector(n,(2 * dot_product)))
	V_dir = vector_math.normalize_vector(vector_math.vector_from_to(eye_point,Pe))
	intensity = vector_math.dot_vector(reflection_vr,V_dir)
	ray = data.Ray(Pe,L_dir)
	inter2 = collisions.find_intersection_points(sphere_list,ray)
	if dot_product>0 and inter2 == []:
		diff_r = sphere.color.r*sphere.finish.diffuse*dot_product*light.color.r
		diff_g = sphere.color.g*sphere.finish.diffuse*dot_product*light.color.g
		diff_b = sphere.color.b*sphere.finish.diffuse*dot_product*light.color.b
		spec_r = light.color.r*sphere.finish.specular*math.pow(intensity,(1/sphere.finish.roughness))
		spec_g = light.color.g*sphere.finish.specular*math.pow(intensity,(1/sphere.finish.roughness))
		spec_b = light.color.b*sphere.finish.specular*math.pow(intensity,(1/sphere.finish.roughness))
		return data.Color(diff_r,diff_g,diff_b),data.Color(spec_r,spec_g,spec_b)
	else :    
		return data.Color(0,0,0), data.Color(0,0,0)


def find_closest(inter,ray):
	close = vector_math.length_vector(vector_math.vector_from_to(ray.pt,inter[0][1]))
	sphere = inter[0][0]
	point = inter[0][1]
	for (s,p) in inter:
		distance = vector_math.length_vector(vector_math.vector_from_to(ray.pt,p))
		if close > distance:
			close = distance
			sphere = s
			point = p
	return sphere, point


def cast_ray(ray,sphere_list,amb,light,eye_point):
	white = data.Color(1.0,1.0,1.0)
	inter = collisions.find_intersection_points(sphere_list,ray)
	if (inter != []):
		closest_sphere, closest_int = find_closest(inter,ray)
		diffuse,spec = comp(sphere_list,inter,light,closest_sphere,closest_int,eye_point)
		val = closest_sphere.finish.ambient
		final_red = (closest_sphere.color.r*val*amb.r)+diffuse.r+spec.r
		final_green = (closest_sphere.color.g*val*amb.g)+diffuse.g+spec.g
		final_blue = (closest_sphere.color.b*val*amb.b)+diffuse.b+spec.b
		new_color = data.Color(final_red,final_green,final_blue)
		return new_color
	else :
		return white


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list,amb,light):
	image = open('image.ppm','w')
	print >> image, 'P3'
	print >> image, width, height
	print >> image, 255

	distx=(max_x-min_x)/float(width)
	disty=(max_y-min_y)/float(height)
	for y in range(height):
		for x in range(width):
			pix_x = min_x + distx*x
			pix_y = max_y - disty*y

			vr = vector_math.vector_from_to(eye_point,data.Point(pix_x,pix_y,0.0))
			ray = data.Ray(eye_point,vr)
			color = cast_ray(ray,sphere_list,amb,light,eye_point)
			print >> image, int(min(color.r*255,255)),int(min(color.g*255,255)),int(min(color.b*255,255))
