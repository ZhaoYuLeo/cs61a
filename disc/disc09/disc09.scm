scm> ; 2 Primitives and Defining Variables
scm> 123
123
scm> #t
True
scm> #f
False
scm> ; 3 Call Expressions
scm> (- 1 1)
0
scm> (/ 8 4 2)
1
scm> (* (+ 1 2) (+ 1 2))
9
scm> ; Questions 3.1
scm> (define a (+ 1 2))
a
scm> (define b (- (+ (* 3 3) 2) 1))
b
scm> (= (modulo b a) (quotient 5 3))
#t
scm> 
scm> ; 4 Special Forms 
scm>
scm> ; If Expression
scm> (if (< 4 5) 1 2)
1
scm> (if #f (/ 1 0) 42)
42
scm> ; Boolean Operators
scm> (and 25 32)
32
scm> (or 1 (/ 1 0)) ; Short-circuits
1
scm> (not (odd? 10))
#t
scm> ; Questions 4.1
scm> (if (or #t (/ 1 0)) 1 (/ 1 0))
1
scm> ((if (< 4 3) + -) 4 100)
-96
scm> ; Lambdas and Defining Functions
scm> (define square (lambda (x) (* x x))) ; Bind the lambda function to the name square
square
scm> (define (square x) (* x x))
square
scm> square
(lambda (x) (* x x))
scm> (square 4)
16
scm> ; Questions 4.2
scm> (define (factorial x) (if (= x 0) 1 (* x (factorial (- x 1)))))
factorial
scm> (factorial 8)
40320
scm> (define (fib n) (
       cond ((= n 0) 0) 
             ((= n 1) 1)
             (#t (+ (fib (- n 1)) (fib (- n 2))))))
fib
scm> (fib 0)
0
scm> (fib 1)
1
scm> (fib 10)
55
scm> ; 5 Pairs and Lists
scm> nil
()
scm> (define lst (cons 1 (cons 2 (cons 3 nil))))
lst
scm> lst
(1 2 3)
scm> (car lst)
1
scm> (cdr lst)
(2 3)
scm> (car (cdr lst))
2
scm> (cdr (cdr (cdr lst)))
()
scm> (cons 1 (cons 2 (cons 3 nil)))
(1 2 3)
scm> (cons 1 (cons (cons 2 (cons 3 nil)) nil))
(1 (2 3))
scm> (define x 2)
x
scm> (define y 3)
y
scm> (list 1 x 3) ; list is a procedure, all operands are evaluated when list is called
(1 2 3)
scm> (quote (1 x 3)) ; quate returns the operand exactly as is, without evaluating it.
(1 x 3)
scm> '(1 x 3) ; Equivalent to the previous quote expression
(1 x 3)
scm> '(+ x y)
(+ x y)
scm> (define a '(1 2 3))
a
scm> (= a a)
Traceback (most recent call last):
 0	(= a a)
Error: operand 0 ((1 2 3)) is not a number
scm> (equal? a '(1 2 3)) ; pairs have the same contents otherwise like eq?
#t
scm> (eq? a '(1 2 3)) ; == for two non-pairs(numbers, etc) otherwise is
#f
scm> (define b a)
b
scm> (eq? a b)
#t
scm> ; Questions
scm> ; 5.1
scm> (define (my-append a b)
      (if (null? a) b
        (cons (car a) (my-append (cdr a) b))
      )
     )
scm> (my-append '(1 2 3) '(2 3 4))
(1 2 3 2 3 4)
scm> (define x (+ 1 2 3))
x
scm> x
6
scm> ; 5.2
scm> (define (x) (+ 1 2 3))
x
scm> x
(lambda () (+ 1 2 3))
scm> (define s '(5 4 (1 2) 3 7))
s
scm> ; selects the value 3 from the list below
scm> (car (cdr (cdr (cdr s))))
3
scm> ; 5.3
scm> ; duplicates every element in the list
scm> (define (duplicate lst) 
      (if (null? lst) lst
        (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
      )
     )
scm> (duplicate '(1 2 3 4))
(1 1 2 2 3 3 4 4)
scm> ;5.4
scm> ; inserts the element into the list at that index
scm> (define (insert element lst index) 
      (if (= index 0) (cons element lst)
        (cons (car lst) (insert element (cdr lst) (- index 1)))
      )
     )
scm> (insert 3 '(1 2 4 5) 2)
(1 2 3 4 5)
