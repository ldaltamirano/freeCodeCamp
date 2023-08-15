class Rectangle:
    width = 0
    height = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return "Rectangle(width="+ str(self.width) +", height="+ str(self.height) +")"
    def set_width(self, width):
       self.width = width
    
    def set_height(self, height):
       self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    def get_picture(self):
        if(self.width > 50 or self.height > 50):
            return "Too big for picture."
        if(self.width == 1 and self.height == 1 ):
            return "*"
        else:
            limitSup = "*"*self.width+ '\n'
            limitInf = "*"*self.width+ '\n'
            rows = ""
            index = 1

            if(self.width == 2 and self.height == 2):
                rows = ""
            elif(self.width-2 == 1):
                while(self.height -1 != index):
                    rows += "***" + '\n'
                    index+=1
            elif(self.height-2 == 1):
                rows += "*"+ "*" * (self.width-2) + "*" + '\n'        
            else:
                while(self.height-2 != index):
                    rows += "*"+ "*" * (self.width-2) + "*" + '\n'        
            return limitSup + rows + limitInf

    
    def get_amount_inside(self, shape):
        print(shape)
        if(shape.width > self.width or shape.height > self.height):
            return 0
        else:
            countWidth = 0
            countHeight = 0
            instanceWidth = self.width
            instanceHeight = self.height
            shapeWidth = shape.width
            shapeHeight = shape.height
            while(instanceWidth >= shapeWidth):
                countWidth += 1
                instanceWidth -= shapeWidth
            while(instanceHeight >= shapeHeight):
                countHeight += 1
                instanceHeight -= shapeHeight
            
            if(countWidth == 0 or countHeight == 0):
                return 0
            else:
                return countWidth * countHeight


class Square(Rectangle):
    def __init__(self, lado):
        self.width = lado
        self.height = lado
    def __str__(self):
        return "Square(side="+ str(self.width) +")"
    
    def set_side(self, lado):
       self.width = lado
       self.height = lado
