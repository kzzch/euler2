#lang racket

(define (euler1)
  (for ([i (in-range 100)])
    (cond
    [(= 0 (modulo i 15)) (printf "FooBar\n")]
    [(= 0 (modulo i 5)) (printf "Bar\n")]
    [(= 0 (modulo i 3)) (printf "Foo\n")]
    [else (printf "~s\n" i)])))
