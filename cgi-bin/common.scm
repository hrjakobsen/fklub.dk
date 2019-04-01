(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  

; HTML mirror loading
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")

(load "/usr/local/cgi-bin/lib/common.scm")
(cgi-lib-load "lib/convenience.scm")

(define menu '(("Hjem" . "/cgi-bin/index.cgi") ("Galleri" . "/cgi-bin/galleri.cgi") ("FAQ" . "/cgi-bin/faq.cgi") ("Kalender" . "/cgi-bin/kalender.cgi")  ("Admin" . "/cgi-bin/admin/index.cgi") ("FIKI" . "http://fff.fklub.dk")))

(define menu-list 
	(map (lambda (x) (div 'class "col" (a 'href (cdr x) (car x)))) menu))

(define fklub-header 
	(div 'class "header" 
			(row 
				menu-list)))

(define (fklub-page page-title x)
	(cgi-write 
		(html
			(head
				(title page-title)
				(meta 'charset "utf-8")
				(link 'rel "stylesheet" 'href "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css")
				(link 'rel "stylesheet" 'href "/style.css"))
			(body 
				(container
					(con 
						fklub-header
						x))))))