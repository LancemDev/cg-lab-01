import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 400, 300)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

ctx.move_to(130, 170)
ctx.line_to(130, 270)
ctx.line_to(260, 270)
ctx.line_to(260, 170)
ctx.set_source_rgb(0,0,0)
ctx.fill_preserve()
ctx.set_source_rgb(1,1,1)
ctx.stroke()

ctx.rectangle(200, 220, 30, 50)
ctx.rectangle(160, 220, 30, 50)
ctx.fill()

ctx.arc(190, 230, 30, math.radians(180), math.radians(270))
ctx.set_source_rgb(1,1,1)
ctx.fill()


surface.write_to_png('church.png')