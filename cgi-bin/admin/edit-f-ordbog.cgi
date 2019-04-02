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

(define entries 
	(let ((data (safe-read "/data/f-ordbog.scm" '()))) 
		(if (list? data) (reverse data) (list))))

(define (dictionary entries) 
	  	(div 
		    (if (null? entries) (p "Ingen opslag")
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
								(td  (cdr x))
								(td 
									(form-1
										"remove-f-ordbog-word.cgi"
										(con
											(hidden-line 'word (car x))
											(submit "Slet")
											)))
							)) entries))
				))

		 	(form-1 
		 		"upload-f-ordbog-word.cgi"
		 		(con 
		 			(text-line 'word 3 "")
		 			(text-line 'meaning 3 "")
		 			(submit "Tilføj ord")
		 		)
		 	)))

(fklub-page "test" (con admin-menu-list (dictionary entries)))

(end)
