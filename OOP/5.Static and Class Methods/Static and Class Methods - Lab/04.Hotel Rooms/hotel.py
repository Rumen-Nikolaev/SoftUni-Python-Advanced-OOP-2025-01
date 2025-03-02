from project.room import Room

class Hotel:
  def __init__(self, name):
    self.name = name
    self.rooms = []
    self.guests = 0

  @classmethod
  def from_stars(cls, stars_count):
    return cls(f"{stars_count} stars Hotel")

  def add_room(self, room: Room):
    self.rooms.append(room)

  def take_room(self, room_number, people):
    f
    
    
