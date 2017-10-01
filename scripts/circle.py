# Prints the coordinates for an svg path curve for a circle centered in a 100x100 viewport
# A scale of 1. will be a circle filling the viewport (diameter 100)

scale = .9

c = 0.55191502449 / 2.0 * 100

points = [
  [0, 50],
  [0, 50 - c],

  [50 - c, 0],
  [50, 0],
  [50 + c, 0],

  [100, 50 - c],
  [100, 50],
  [100, 50 + c],

  [50 + c, 100],
  [50, 100],
  [50 -c, 100],

  [0, 50 + c],
  [0, 50],
  [0, 50 - c],
];

def adj(x):
  return scale * x + (1.0 - scale) * 50

points = [[adj(p[0]), adj(p[1])] for p in points]

curve_string = ' '.join([('%.3f' % p[0]) + ',' + ('%.3f' % p[1]) for p in points[1:]])

print 'M %.3f,%.3f C %s' % (points[0][0], points[0][1], curve_string)
