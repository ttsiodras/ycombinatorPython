#!/usr/bin/env python2

fx = (lambda improver2: improver2(improver2))( lambda improver: lambda n: 1 if n == 0 else n*improver(improver)(n-1) )

print "50! =", fx(50)
