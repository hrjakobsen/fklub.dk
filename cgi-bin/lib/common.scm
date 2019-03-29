(define (eq-lookup symbol a-list)
    (if (null?  a-list) #f
        (if (equal? (caar a-list) symbol) 
            (cdar a-list)
            (eq-lookup symbol (cdr a-list)))))

(define (negate-n f)
    (lambda (x . y)
       (not (apply f (cons x y)))))

(define (random-string size)
    (if (= 0 size) ""
        (let* (
            (acceptable-chars '("a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z"))
            (len (length acceptable-chars)))
            (string-append (list-ref acceptable-chars (random len)) (random-string (- size 1))))))