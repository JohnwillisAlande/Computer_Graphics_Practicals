import cairo

# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
context = cairo.Context(surface)
context.set_source_rgb(0.8,0.8,0.8)
context.paint()

# Set line color and width
context.set_source_rgb(0,0,0)
context.set_line_width(10)

# """LINE CAPS"""
# # Butt Cap
# context.move_to(100,80)
# context.line_to(500,80)
# context.set_line_cap(cairo.LINE_CAP_BUTT)
# context.stroke()
#
# # Square Cap
# context.move_to(100,200)
# context.line_to(500,200)
# context.set_line_cap(cairo.LINE_CAP_SQUARE)
# context.stroke()
#
# # Round Cap
# context.move_to(100,320)
# context.line_to(500,320)
# context.set_line_cap(cairo.LINE_CAP_ROUND)
# context.stroke()


# """LINE JOINS"""
# #Miter join
# context.move_to(50,100)
# context.line_to(180,300)
# context.line_to(50,300)
# context.set_line_join(cairo.LINE_JOIN_MITER)
# context.stroke()
#
# #Round Join
# context.move_to(240,100)
# context.line_to(370,300)
# context.line_to(240,300)
# context.set_line_join(cairo.LINE_JOIN_ROUND)
# context.stroke()
#
# #Bevel Join
# context.move_to(430,100)
# context.line_to(560,300)
# context.line_to(430,300)
# context.set_line_join(cairo.LINE_JOIN_BEVEL)
# context.stroke()

"""DASHED LINES"""
#1
context.move_to(100,50)
context.line_to(500,50)
context.set_dash([20])
context.stroke()

#2
context.move_to(100,100)
context.line_to(500,100)
context.set_dash([20,10])
context.stroke()

#3
context.move_to(100,150)
context.line_to(500,150)
context.set_dash([20,5,5,5])
context.stroke()

#4
context.move_to(100,200)
context.line_to(500,200)
context.set_dash([5,5,10])
context.stroke()

context.set_line_width(10)
context.set_line_cap(cairo.LINE_CAP_ROUND)

#5
context.move_to(100,250)
context.line_to(500,250)
context.set_dash([10,20])
context.stroke()

#6
context.move_to(100,300)
context.line_to(500,300)
context.set_dash([0,20])
context.stroke()

surface.write_to_png('lines.png')