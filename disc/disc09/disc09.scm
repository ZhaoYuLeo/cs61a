scm> 123
123
scm> #t
True
scm> #f
False
scm>
scm> (- 1 1)
0
scm> (/ 8 4 2)
1
scm> (* (+ 1 2) (+ 1 2))
9
scm>
scm> (define a (+ 1 2))
a
scm> (define b (- (+ (* 3 3) 2) 1))
b
scm> (= (modulo b a) (quotient 5 3))
#t
scm> 
scm>  
scm> (if (< 4 5) 1 2)
1
scm> (if #f (/ 1 0) 42)
42
scm> (and 25 32)
32
scm> (or 1 (/ 1 0)) ; Short-circuits
1
scm> (not (odd? 10))
#t
scm>
scm> (if (or #t (/ 1 0)) 1 (/ 1 0))
1
scm> ((if (< 4 3) + -) 4 100)
-96
scm> (define square (lambda (x) (* x x))) ; Bind the lambda function to the name square
square
scm> (define (square x) (* x x))
square
scm> square
(lambda (x) (* x x))
scm> (square 4)
16

