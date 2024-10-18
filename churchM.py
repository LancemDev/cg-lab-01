import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 400,300)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

#Shell
#side rects
ctx.rectangle(50, 220, 80, 40)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(3)
ctx.stroke()
ctx.rectangle(260, 220, 80, 40)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(3)
ctx.stroke()

#small white
ctx.rectangle(60, 230, 20, 15)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()
ctx.rectangle(90, 230, 20, 15)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()
ctx.rectangle(280, 230, 20, 15)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()
ctx.rectangle(310, 230, 20, 15)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

#trapeziums
ctx.move_to(80, 190)
ctx.line_to(130, 190)
ctx.line_to(130, 220)
ctx.line_to(40, 220)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(1)
ctx.stroke()

ctx.move_to(260, 190)
ctx.line_to(310, 190)
ctx.line_to(350, 220)
ctx.line_to(260, 220)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(1)
ctx.stroke()

#Center
ctx.move_to(130, 170)
ctx.line_to(130, 270)
ctx.line_to(260, 270)
ctx.line_to(260, 170)
ctx.set_source_rgb(0,0,0)
ctx.fill_preserve()
ctx.set_source_rgb(1,1,1)
ctx.stroke()

ctx.rectangle(160, 220, 34, 47)
ctx.rectangle(196, 220, 34, 47)
ctx.fill()

ctx.move_to(160, 220)
ctx.curve_to(170, 210, 180, 210, 194, 210)
ctx.line_to(194, 220)
ctx.close_path()
ctx.fill()

ctx.move_to(196, 210)
ctx.curve_to(210, 210, 220, 210, 229, 220)
ctx.line_to(196, 220)
ctx.close_path()
ctx.fill()

surface.write_to_png('lab.png')