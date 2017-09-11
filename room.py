class room_gen_options:
	"""options for room generation"""
	def __init__(self, x_size, y_size, nb_trap, wall_ratio, room_type):
		self.x_size = int(x_size)
		self.y_size = int(y_size)
		self.nb_trap = int(nb_trap)
		self.wall_ratio = wall_ratio
		self.room_type = room_type

class room:
	"""creating a room"""
	def __init__(self, array_map, room_gen_options):
		self.array_map = array_map
		self.room_gen_options = room_gen_options
