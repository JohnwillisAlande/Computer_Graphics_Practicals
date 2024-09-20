import cairo

# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
context = cairo.Context(surface)
context.set_source_rgb(0.8,0.8,0.8)
context.paint()

# Set line color and width
context.set_source_rgb(0,0,0)
context.set_line_width(20)

"""LINE CAPS"""
# Butt Cap
context.move_to(100,80)
context.line_to(500,80)
context.set_line_cap(cairo.LINE_CAP_BUTT)
context.stroke()

# Square Cap
context.move_to(100,200)
context.line_to(500,200)
context.set_line_cap(cairo.LINE_CAP_SQUARE)
context.stroke()

# Round Cap
context.move_to(100,320)
context.line_to(500,320)
context.set_line_cap(cairo.LINE_CAP_ROUND)
context.stroke()

surface.write_to_png('lines.png')