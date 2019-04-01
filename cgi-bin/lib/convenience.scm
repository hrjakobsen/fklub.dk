(define (make-div-alias class)
    (lambda (x . rest) (div 'class class (con (cons x rest)))))

(define container (make-div-alias "container"))
(define row (make-div-alias "row"))

(define (col classes x)
   (div 'class classes x)) 

(define (card title image-src text link-text link-src)
    (div 'class "card"
        (img 'class "card-img-top" 'src image-src)
        (div 'class "card-body"
          (h5 'class "card-title" title)
          (p 'class "card-text" text)
          (a 'href link-src 'class "btn btn-primary" link-text))))