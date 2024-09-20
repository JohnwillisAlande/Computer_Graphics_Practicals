import cairo

#Set up pycairo
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
context = cairo.Context(surface)
context.set_source_rgb(0.8,0.8,0.8)
context.paint()

# #Bezier curve
# context.move_to(100,200)
# context.curve_to(200,100,400,300,500,200)
# context.set_source_rgb(1,0,0)
# context.set_line_width(10)
# context.stroke()

# Joining curves and lines to form poly curves
context.move_to(100,100)
context.curve_to(200,0,400,200,500,100)
context.line_to(500,300)
context.curve_to(400,400,200,200,100,300)
context.close_path()
context.set_source_rgb(1,0,0)
context.set_line_width(10)
context.stroke()

surface.write_to_png('bezierCurve.png')