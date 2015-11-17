#!/usr/bin/env node
Y = function (builder, n) { return builder(builder, n); };

fact_helper = function (builder, n) { if (n == 0) return 1; else return n * builder(builder, n - 1); };

fact = function(n) { return Y(fact_helper, n); };

console.log(fact(21));
