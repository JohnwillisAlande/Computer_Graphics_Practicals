import cairo

# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
context = cairo.Context(surface)
context.set_source_rgb(0.8, 0.8, 0.8)
context.paint()

# Closed Polygon
context.move_to(50, 100) #A
context.line_to(200, 50) #B
context.line_to(250, 300) #C
context.line_to(100, 200) #D
context.close_path() #To make an open polygon, just omit this line
context.set_source_rgb(1, 0, 0)
context.set_line_width(10)
context.stroke()

surface.write_to_png('polygon.png')