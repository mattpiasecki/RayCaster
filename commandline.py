import data
import sys

def reader(file_num):
	try:
		read = open(sys.argv[file_num],'r')
		return read
	except IOError:
		print 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
		sys.exit()

def file_to_sphere_list(read):
	sphere_list = []
	counter = 0
	for i in read:
		line = i.split()
		counter+= 1
		try:
			if(len(line)>11):
				tester = line[99] #return an index error 
			x = float(line[0]) 
			y = float(line[1])
			z = float(line[2])
			pt = data.Point(x,y,z)
			radius = float(line[3]) 
			r = float(line[4])
			g = float(line[5])
			b = float(line[6])
			sphere_color = data.Color(r,g,b)
			ambient = float(line[7])
			diffuse = float(line[8])
			specular = float(line[9])
			roughness = float(line[10])
			sphere_finish = data.Finish(ambient,diffuse,specular,roughness)
			sphere1 = data.Sphere(pt,radius,sphere_color,sphere_finish)
			sphere_list.append(sphere1)
		except IndexError:
			print 'malformed sphere on line '+ str(counter) +' ... skipping'
		except TypeError:
			print 'malformed sphere on line '+ str(counter) +' ... skipping'
		except ValueError:
			print 'malformed sphere on line '+ str(counter) +' ... skipping'
	return sphere_list	

def check_eye():
	try:
		if '-eye' in argv:
			i = argv.index('-eye')
			x = float(sys.argv[i+1])
			y = float(sys.argv[i+2])
			z = float(sys.argv[i+3])
			return data.Point(x,y,z)		
		else :
			x = 0.0
			y = 0.0
			z = -14.0
			return data.Point(x,y,z)
	except :
		x = 0.0
		y = 0.0
		z = -14.0
		return data.Point(x,y,z)

def check_view():
	try:
		if '-view' in sys.argv:
			i = sys.argv.index('-view')
			min_x = float(sys.argv[i+1])
			max_x = float(sys.argv[i+2])
			min_y = float(sys.argv[i+3])
			max_y = float(sys.argv[i+4])
			width = int(sys.argv[i+5])
			height = int(sys.argv[i+6])
			return min_x,max_x,min_y,max_y,width,height
		else :
			min_x = -10
			max_x = 10
			min_y = -7.5
			max_y = 7.5
			width = 1024
			height = 768
			return min_x,max_x,min_y,max_y,width,height	
	except :
		min_x = -10
		max_x = 10
		min_y = -7.5
		max_y = 7.5
		width = 1024
		height = 768
		return min_x,max_x,min_y,max_y,width,height

def check_light():
	try:
		if '-light' in sys.argv:
			i = sys.argv.index('-light')
			x = float(sys.argv[i+1])
			y = float(sys.argv[i+2])
			z = float(sys.argv[i+3])
			r = float(sys.argv[i+4])
			g = float(sys.argv[i+5])
			b = float(sys.argv[i+6])
			pt = data.Point(x,y,z)
			color = data.Color(r,g,b)
			light = data.Light(pt,color)
			return light
		else :
			x = -100.0
			y = 100.0
			z = -100.0
			r = 1.5
			g = 1.5
			b = 1.5
			pt = data.Point(x,y,z)
			color = data.Color(r,g,b)
			light = data.Light(pt,color)
			return light
	except :
		x = -100.0
		y = 100.0
		z = -100.0
		r = 1.5
		g = 1.5
		b = 1.5
		pt = data.Point(x,y,z)
		color = data.Color(r,g,b)
		light = data.Light(pt,color)
		return light
		

def check_ambient():
	try:
		if '-ambient' in sys.argv:
			i = sys.argv.index('-ambient')
			r = float(sys.argv[i+1])
			g = float(sys.argv[i+2])
			b = float(sys.argv[i+3])
			return data.Color(r,g,b)
		else :
			r = 1.0
			g = 1.0
			b = 1.0
			return data.Color(r,g,b)
	except :
		r = 1.0
		g = 1.0
		b = 1.0
		return data.Color(r,g,b)
		
