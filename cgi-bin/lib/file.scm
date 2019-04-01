(define (swap f) (lambda (x y) (f y x)))

(define read-data-file file-read)

(define (write-data-file file data)
(begin
	(define out (open-output-file file 'truncate/replace))
	(write data out)
	(close-output-port out)
	))


;(define write-data-file (swap file-write))

(define (id x) x)

(define (dir-list dir) (directory-list dir))

(define (get-files dir) 
	(filter (negate directory-exists?) (directory-list dir)))

(define (ensure-exists dir) 
	(if (directory-exists? dir) #t (make-directory dir)))