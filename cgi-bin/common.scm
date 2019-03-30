(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  

; HTML mirror loading
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")

(define menu '(("Galleri" . "/cgi-bin/galleri.cgi") ("FAQ" . "/cgi-bin/faq.cgi") ("Kalender" . "/cgi-bin/kalender.cgi") ("Cookie" . "/cgi-bin/cookie.cgi") ("Login" . "/cgi-bin/login.cgi") ("FIKI" . "http://fff.fklub.dk")))

(define menu-list 
	(ul
		(map (lambda (x) (li (a 'href (cdr x) (car x)))) menu)
	))
