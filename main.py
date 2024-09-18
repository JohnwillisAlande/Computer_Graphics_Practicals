"""This is the  module that runs the whole code base"""
import rectangle

OUTPUT_DIR = 'output_dir/'
WIDTH, HEIGHT = 600, 400

if __name__ == '__main__':
    bg_color = (0.8, 0.8, 0.8)
    shape_color = (1, 0, 0)

    surface, context = rectangle.create_surface(WIDTH, HEIGHT, bg_color)
    rectangle.draw_rectangle(context, 100, 100, 100, 240, shape_color)
    surface.write_to_png(f'{OUTPUT_DIR}new_rectangle.png')
    print('Done!')
