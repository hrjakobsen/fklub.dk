(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  

; HTML mirror loading
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")

(define menu '(("Galleri" . "galleri.cgi") ("FAQ" . "faq.cgi") ("Kalender" . "kalender.cgi")))

(define menu-list 
	(ul
		(map (lambda (x) (li (a 'href (cdr x) (car x)))) menu)
	))

(define (redirect x) (display (string-append "Location: " x "\n\n")))

(define (read-data-file file)
	(if (file-exists? file)
		(let* (
			(in (open-input-file file))
			(raw-data (read in))
		) (begin
			(close-input-port in)
			raw-data
		))
		#f 
	))

(define (write-data-file file data)
	(begin
		(define out (open-output-file file 'truncate/replace))

		(write data out)

		(close-output-port out)))