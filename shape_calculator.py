class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self,num):
    self.width = num

  def set_height(self,num):
    self.height = num
  
  def get_area(self):
    return self.width*self.height
  
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    img = ""
    if(self.width > 50 or self.height > 50):
      return "Too big for picture."
    for i in range(self.height):
      img = img + "*"*self.width + "\n"
    return img

  def get_amount_inside(self, shape):
    count = 0
    area = self.get_area()
    other = shape.get_area()
    while area>= other:
      count += 1
      area -= other
    return count
      

  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.width, self.height)

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, num):
    self.width = num
    self.height = num

  def __str__(self):
    return "Square(side={})".format(self.width)
