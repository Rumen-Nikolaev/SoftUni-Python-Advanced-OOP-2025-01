class DVD:
  def __init__(self, name, id, creation_year, creation_month, age_restriction):
    self.name = name
    self.id = id
    self.creation_year = creation_year
    self.creation_month = creation_month
    self.age_restriction = age_restriction
    self.is_rented = False

  def from_date(self, id, name, date, age_restriction):
    
