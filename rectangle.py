"""This module draws a rectangle on a canvas"""
import cairo

# # Setting up the surface (Before Refactoring)
# surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
# context = cairo.Context(surface)
# context.set_source_rgb(0.8, 0.8, 0.8)
# context.paint()

# Setting up the canvas
def create_surface(width, height, background_color):
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)
    context.set_source_rgb(*background_color)
    return surface, context

# Drawing the rectangle on the canvas
def draw_rectangle(context, x, y, width, height, color):
    context.rectangle(x, y, width, height)
    context.set_source_rgb(*color)
    context.fill()

# # Drawing the rectangle on the canvas
# context.rectangle(0,0,100,240)
# context.set_source_rgb(1,0,0)
# context.fill()
#
# surface.write_to_png('rectangle.png')