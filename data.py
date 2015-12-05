import utility

class Point(object):
	def __init__(self, x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def __eq__(self,other):
		if (utility.epsilon_equal(self.x,other.x)
		& utility.epsilon_equal(self.y,other.y)
		& utility.epsilon_equal(self.z,other.z)):
			return True
		else :
			return False

class Vector(object):
	def __init__(self, x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def __eq__(self,other):
		if (utility.epsilon_equal(self.x,other.x)
		& utility.epsilon_equal(self.y,other.y)
		& utility.epsilon_equal(self.z,other.z)):
			return True
		else :
			return False

class Ray(object):
	def __init__(self, pt,dir):
		self.pt = pt
		self.dir = dir
	def __eq__(self,other):
		if (utility.epsilon_equal(self.pt.x,other.pt.x)
		& utility.epsilon_equal(self.pt.y,other.pt.y)
		& utility.epsilon_equal(self.pt.z,other.pt.z)
		& utility.epsilon_equal(self.dir.x,other.dir.x)
		& utility.epsilon_equal(self.dir.y,other.dir.y)
		& utility.epsilon_equal(self.dir.z,other.dir.z)):
			return True
		else :
			return False

class Sphere(object):
	def __init__(self,center,radius,color,finish):
		self.center = center
		self.radius = radius
		self.color = color
		self.finish = finish
	def __eq__(self, other):
		if (utility.epsilon_equal(self.center.x,other.center.x)
		& utility.epsilon_equal(self.center.y,other.center.y)
		& utility.epsilon_equal(self.center.z,other.center.z)
		& utility.epsilon_equal(self.radius,other.radius)
		& utility.epsilon_equal(self.color,other.color)
		& utility.epsilon_equal(self.finish.ambient,other.finish.ambient)
		& utility.epsilon_equal(self.finish.diffuse,other.finish.diffuse)):
			return True
		else :
			return False

class Color(object):
	def __init__(self,r,g,b):
		self.r = r
		self.g = g
		self.b = b
	def __eq__(self, other):
		if (utility.epsilon_equal(self.r,other.r)
		& utility.epsilon_equal(self.g,other.g)
		& utility.epsilon_equal(self.b,other.b)):
			return True
		else :
			return False	

class Finish(object):
	def __init__(self,ambient,diffuse,specular,roughness):
		self.ambient = ambient
		self.diffuse = diffuse
		self.specular = specular
		self.roughness = roughness
	def __eq__(self, other):
		if (utility.epsilon_equal(self.ambient,other.ambient)
		& utility.epsilon_equal(self.diffuse,other.diffuse)
		& utility.epsilon_equal(self.specular,other.specular)
		& utility.epsilon_equal(self.roughness,other.roughness)):
			return True
		else :
			return False

class Light(object):
	def __init__(self,pt,color):
		self.pt = pt
		self.color = color
	def __eq__(self, other):
		if (utility.epsilon_equal(self.pt.x,other.pt.x)
		&	utility.epsilon_equal(self.pt.y,other.pt.y)
		&	utility.epsilon_equal(self.pt.z,other.pt.z)
		&	utility.epsilon_equal(self.color.r,other.color.r)
		&	utility.epsilon_equal(self.color.g,other.color.g)
		&	utility.epsilon_equal(self.color.b,other.color.b)):
			return True
		else :
			return False					