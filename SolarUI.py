from tkinter import *
import math

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.canvas_width = 200  # Assume canvas width is 400 pixels
        self.canvas_height = 250  # Assume canvas height is 400 pixels
        self.radius = 100  # Radius of the circle
        self.angle = 0  # Current angle for rotation
        self.black_hole_radius = 10  # Radius of the black circle
        self.angle = 0  # Current angle for rotation
        self.initUI()
    
    def initUI(self):
        self.master.title("Rotating Oval")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.solar = self.canvas.create_oval(self.canvas_width, self.canvas_width,
                                             self.canvas_height, self.canvas_height,
                                             outline="#f11", fill="#fdfbd3")

        # Create black circle at the center
        center_x = self.canvas_width // 4 # FAUX
        center_y = self.canvas_height // 4 # FAUX
        self.black_hole = self.canvas.create_oval(137.5,
                                                   162.5,
                                                   147.5,
                                                   172.5,
                                                   outline="#000", fill="#000")
        self.canvas.pack(fill=BOTH, expand=1)

        self.after(2000, self.updateUI)  # Schedule update every 20 milliseconds
    

    def updateUI(self):
        # Calculate new coordinates based on angle and radius
        center_x = self.canvas_width #// 2  # Center X using floor division
        center_y = self.canvas_height #// 2  # Center Y using floor division
        x_offset = self.radius * math.cos(math.radians(self.angle))
        y_offset = self.radius * math.sin(math.radians(self.angle))

        # Calculate relative coordinates from center
        rel_x = center_x + x_offset - self.radius
        rel_y = center_y + y_offset - self.radius
        # Update the oval's position using move
        self.canvas.move(self.solar, rel_x - self.canvas.coords(self.solar)[0],
                     rel_y - self.canvas.coords(self.solar)[1])


        # Update the angle for the next rotation
        self.angle += 1 # Adjust rotation speed (degrees per update)

        # Wrap the angle around 360 degrees to keep rotation continuous
        self.angle %= 360

        self.after(10, self.updateUI)  # Schedule next update
    

def main():
  root = Tk()
  ex = Example()
  root.geometry("400x400+600+200")
  root.mainloop()

if __name__ == '__main__':
  main()
