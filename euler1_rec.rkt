#lang racket
(define (euler1 x)
  (cond
    [(= 0 (modulo x 15)) 'FooBar]
    [(= 0 (modulo x 5)) 'Bar]
    [(= 0 (modulo x 3)) 'Foo]
    [else x]))

(define (solution x)
  (cond
    [(= x 100) (euler1 x)]
    [else (solution (+ x 1))]))