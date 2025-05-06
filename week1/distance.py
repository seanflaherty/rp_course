class Distance(float):
   def __new_(cls, value, unit):
    instance =  super().__init(cls, value)
    instance.unit = unit
    return instance
   
in_miles = Distance(33.0, "Miles")