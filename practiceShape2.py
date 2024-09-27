import cairo

"""2 triangles inverted"""
# Set up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
context = cairo.Context(surface)
context.set_source_rgb(0.8,0.8,0.8)
context.paint()

context.set_line_width(15)
context.rectangle(50,50,300,200)
context.fill_preserve()
context.stroke()

# Inner red triangle
context.set_source_rgb(1,0,0)
context.move_to(60,53)
context.line_to(347,53)
context.line_to(347,242)
context.close_path()
context.fill_preserve()
context.set_line_join(cairo.LINE_JOIN_ROUND)
context.stroke()

# Black triangle outline
context.set_source_rgb(0,0,0)
context.set_line_width(10)
context.move_to(50,50)
context.line_to(350,50)
context.line_to(350,250)
context.close_path()
context.set_line_join(cairo.LINE_JOIN_ROUND)
context.stroke()

# Black triangle outline
context.set_source_rgb(1,0,0)
context.set_line_width(10)
context.move_to(50,80)
context.line_to(50,280)
context.line_to(350,280)
context.close_path()
context.set_line_join(cairo.LINE_JOIN_ROUND)
context.stroke()

surface.write_to_png("practiceShape2.png")