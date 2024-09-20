import cairo
import math

# Set up PyCairo
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
context = cairo.Context(surface)
context.set_source_rgb(0.8, 0.8, 0.8)
context.paint()

# Draw an arc
context.arc(300, 200, 150, 0, math.pi/2)
context.set_source_rgb(1,0,0)
context.set_line_width(10)
context.stroke()

surface.write_to_png('arc.png')