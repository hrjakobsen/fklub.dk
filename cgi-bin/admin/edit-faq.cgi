#!/usr/bin/plt/bin/mzscheme -r

(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  

; HTML mirror loading
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")

(define cgi-testing #f)

(load "/usr/local/cgi-bin/lib/common.scm")
(cgi-lib-load "admin/admin.scm")
(cgi-lib-load "common.scm")
(cgi-lib-load "lib/file.scm")

(ensure-admin)

(define questions 
	(let ((data (safe-read "/data/faq.scm" '()))) 
		(if (list? data) (reverse data) (list))))

(define (faq questions) 
	  	(div 
		    (if (null? questions) (p "Ingen spørgsmål")
				(table 'border 1
					(thead
						(tr
							(th "Spørgsmål")
							(th "Svar")
							(th "Slet")))
					(tbody 
						(map (lambda (x) 
							(tr 
								(td (car x))
								(td (cdr x))
								(td 
									(form-1
										"remove-faq.cgi"
										(con
											(hidden-line 'question (car x))
											(submit "SLET")))
								))) questions)))
				)

		 	(form-1 
		 		"upload-faq.cgi"
		 		(con 
		 			(text-line 'question 3 "")
		 			(text-line 'answer 3 "")
		 			(submit "Tilføj FAQ")
		 		)
		 	)))

(fklub-page "test" (con admin-menu-list (faq questions)))

(end)
