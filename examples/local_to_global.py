def global_to_local(z,z_e):
	"""converts global coordinate to local(element) coordinate.
	Parameters
	z:float
	  The global coordinate to convert to local coordinate
	z_e:array_like, shape=(2,)
	   Nodal coordinates of the element
	Returns
	floats
	    The local coordinate
	"""
	return (z-z_e(0))-(z_e(1)-z_e(0))