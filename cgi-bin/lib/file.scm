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

(define (ensure-file-exists path default-data)
	(if (file-exists? path) #t (write-data-file path default-data)))
	
(define (safe-read path data)
	(ensure-file-exists path data)
	(read-data-file path))

(define (get-last-edit file) (seconds->date (file-or-directory-modify-seconds file)))

(define (in-gallery? str) (in-gallery-char? (string->list str)))

(define (in-gallery-char? char-list)
	(if (null? char-list) #t
		(let ((first (car char-list)))
			(and (not (eq? first #\.))
			     (not (eq? first #\/))
				 (in-gallery-char? (cdr char-list))))))