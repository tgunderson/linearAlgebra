"""This is for practicing Linear Algebra"""
"""It is also for practicing using Git"""
"""This is for practicing commits"""

from math import sqrt, acos, pi, degrees
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

	CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'	
	
	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple([Decimal(x) for x in coordinates])
			self.dimension = len(self.coordinates)
			
		except ValueError:
			raise ValueError('The coordinates must be nonempty')
		
		except TypeError:
			raise TypeError('The coordinates must be an iteratable')
			
	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)	
	
	def __eq__(self, v):
		return self.coordinates == v.coordinates
		

	def plus(self, v):
		new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordinates)
	
	def minus(self,v):
		new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordinates)
		
	def times_scalar(self, c):
		new_coordinates = [Decimal(c)*x for x in self.coordinates]
		return Vector(new_coordinates)
		
	def magnitude(self):
		magna = [x**2 for x in self.coordinates]
		return sqrt(sum(magna))
		
	def normalization(self):
		try:
			return self.times_scalar(Decimal('1.0')/Decimal(self.magnitude()))
		
		except ZeroDivisionError:
			raise Exception('Cannot normalize the zero vector')
			
	def dot_product(self, c):
		return sum([x*y for x,y in zip(self.coordinates, c.coordinates)])
		
	def inner_product(self, c):
		return acos(self.dot_product(c)/(self.magnitude() * c.magnitude()))
		
	def angle_with(self, v, in_degrees=False):
		try:
			u1 = self.normalization()
			u2 = v.normalization()
			angle_in_radians = acos(u1.dot_product(u2))
			
			if in_degrees:
				return degrees(angle_in_radians)
			else:
				return angle_in_radians
				
		except Exception as e:
			if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
				raise Exception('Cannot compute an angle with the zero vector')
			else:
				raise e	


	def is_parallel(self, v):
		scalar = Decimal(self.coordinates[0]) / Decimal(v.coordinates[0])
		x = 0
		for _ in self.coordinates:
			if self.coordinates[x] != (v.coordinates[x] * scalar):
				return False
			x = x+1
		return True
		
	
	def is_ortho(self, v):
		return (self.dot_product(v) == 0)
		
v = Vector([-7.579,-7.88])		
w = Vector([22.737,23.64])
print (v.is_parallel(w))
print (v.is_ortho(w))

v = Vector([-2.029,9.97,4.172])		
w = Vector([-9.231,-6.639,-7.245])
print (v.is_parallel(w))
print (v.is_ortho(w))

v = Vector([-2.328,-7.284,-1.214])		
w = Vector([-1.821,1.072,-2.94])
print (v.is_parallel(w))
print (v.is_ortho(w))

v = Vector([2.118,4.827])		
w = Vector([0,0])
print (v.is_parallel(w))
print (v.is_ortho(w))

"""

"""


"""
v = Vector([7.887,4.138])
#-69.421374
w = Vector([-8.802,6.776])
print (v.dot_product(w))

v = Vector([-5.955,-4.904,-1.874])
w = Vector([-4.496,-8.755,7.103])
print (v.dot_product(w))

v = Vector([3.193,-7.627])
w = Vector([-2.668,5.319])
print ((v.angle_with(w)))

v = Vector([7.35,0.221,5.188])
w = Vector([2.751,8.259,3.985])
print((v.angle_with(w,True)))
"""


"""
v = Vector([-0.221,7.437])
print (v.magnitude())

v = Vector([8.813,-1.331,-6.247])
print (v.magnitude())

v = Vector([5.581,-2.136])
print (v.normalization())

v = Vector([1.996,3.108,-4.554])
print (v.normalization())
	
	
v = Vector([8.218,-9.341])
w = Vector([-1.120,2.111])
print (v.plus(w))

v = Vector([7.119,8.215])
w = Vector([-8.223,0.878])
print (v.minus(w))

v = Vector([1.671, -1.012,-0.318])
c = 7.41
print (v.times_scalar(c))
	
my_vector = Vector([1,2,3])
print (my_vector)
my_vector2 = Vector([1,2,3])
my_vector3 = Vector([-1,2,3])

print (my_vector == my_vector2)
print (my_vector2 == my_vector3)
"""