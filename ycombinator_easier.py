#!/usr/bin/env python2
from functools import partial

Y = lambda builder,n: builder(builder,n)

fact_helper = lambda builder,n: 1 if n == 0 else n*builder(builder,n-1)

fact = partial(Y, fact_helper)

print "21! =", fact(21)
