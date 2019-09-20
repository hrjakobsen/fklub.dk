(define (get-date-string date)
    (string-append (number->string (date-day date)) "/" (number->string (date-month date)) "/" (number->string (date-year date))))