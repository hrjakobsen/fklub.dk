(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  

; HTML mirror loading
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")

(define menu '(("Galleri" . "galleri.cgi") ("FAQ" . "faq.cgi") ("Kalender" . "kalender.cgi") ("Cookie" . "cookie.cgi") ("Login" . "login.cgi")))

(define menu-list 
	(ul
		(map (lambda (x) (li (a 'href (cdr x) (car x)))) menu)
	))


