class map_gen_options:
	"""options for map generation"""
	def __init__(self, map_size, trap_ratio, max_room_size, min_room_size, average_room_size):
		self.map_size = map_size
		self.trap_ratio = trap_ratio
		self.max_room_size = max_room_size
		self.min_room_size = min_room_size
		self.average_room_size = average_room_size
		

class map:
	"""create a map"""
	def __init__(self, array_room, map_gen_options):
		self.array_room = []
		self.map_gen_option = map_gen_options