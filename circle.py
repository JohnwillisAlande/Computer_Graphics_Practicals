import cairo
import math

# Set up pycairo
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
context = cairo.Context(surface)
context.set_source_rgb(0.8, 0.8, 0.8)
context.paint()

# Small circle
context.arc(300, 200, 50, 0, 2*math.pi)
context.set_source_rgb(0,0,0)
context.set_line_width(10)
context.stroke()

# Medium circle
context.arc(300, 200,100,0,2*math.pi)
context.set_source_rgb(0,0,0)
context.set_line_width(10)
context.stroke()

# Large circle
context.arc(300,200,150,0,2*math.pi)
context.set_source_rgb(0,0,0)
context.set_line_width(10)
context.stroke()

surface.write_to_png('circle.png')