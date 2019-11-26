;; If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
;; The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
;; 233168

(define (sum-mul-of m n l)    
    (if (null? l)
        0
        (cond ((= 0 (remainder (car l) m)) (+ (car l) (sum-mul-of m n (cdr l))))
              ((= 0 (remainder (car l) n)) (+ (car l) (sum-mul-of m n (cdr l))))
              (else (sum-mul-of m n (cdr l))))))

(display (sum-mul-of 3 5 (iota 1000)))
(newline)
