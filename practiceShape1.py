import cairo

"""Sine-like curve with 2 red lines"""
# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
context = cairo.Context(surface)
context.set_source_rgb(0.8,0.8,0.8)
context.paint()

# Black sine-like curve
context.set_source_rgb(0,0,0)
context.set_line_width(10)

#Black colour
context.move_to(50,150)
context.curve_to(210,380,410,10,550,220)
context.stroke()

#Red lines
context.set_source_rgb(1,0,0)
context.set_line_width(5)

# Red colour
context.move_to(50,150)
context.line_to(200,350)
context.stroke()

context.move_to(400,30)
context.line_to(550,220)
context.stroke()

surface.write_to_png('practiceShape1.png')