import cairo

# Set up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
context = cairo.Context(surface)
context.set_source_rgb(0.8,0.8,0.8)
context.paint()

# Sub-path 1
context.move_to(50,50)
context.line_to(400,200)
context.line_to(50,350)
context.close_path()

# Sub-path 2
context.move_to(450,100)
context.line_to(550,100)
context.line_to(450,300)

# Sub-path 3
context.move_to(100,100)
context.line_to(200,200)
context.line_to(100,300)
context.close_path()

context.set_source_rgb(1,0,0)
context.set_line_width(10)
context.stroke()

surface.write_to_png('subPath.png')