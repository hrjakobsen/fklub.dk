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

(define (fa icon) (i 'class (string-append "fa fa-" icon)))

(define menu (list '("Hjem" . "/cgi-bin/index.cgi") '("Galleri" . "/cgi-bin/galleri.cgi") '("FAQ" . "/cgi-bin/faq.cgi") '("F-ordbog" . "/cgi-bin/f-ordbog.cgi") '("Kalender" . "/cgi-bin/kalender.cgi")  '("FIKI" . "http://fff.fklub.dk") (cons (fa "lock")  "/cgi-bin/admin/index.cgi")))

(define menu-list 
	(map (lambda (x) (div 'class "col" (a 'class "menu-link" 'href (cdr x) (car x)))) menu))

(define fklub-header 
	(div 'class "header" 
			(container
				(div 'class "menu"
					(row (con (div 'class "col" (a 'href "/cgi-bin/index.cgi" (img 'class "fklub-logo" 'src "/images/fklub_logo.svg"))) menu-list))))))

(define fklub-footer
	(div 'class "footer"
		(container 
			(div 'class "slider"
        		(p 'class "rolling" (con "Siden er udviklet i " (a 'href "http://people.cs.aau.dk/~normark/laml/" "LAML") " af FIT &mdash; F-klubbens IT udvalg"))))))

(define (heading title) 
	(h1 title))

(define (fklub-page page-title x)
	(cgi-write 
		(html
			(head
				(title (string-append page-title " - Fklub.dk"))
				(meta 'charset "utf-8")
				(meta 'http-equiv "X-UA-Compatible" 'content "IE=edge")
				(link 'rel "stylesheet" 'href "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css")
				(link 'rel "stylesheet" 'href "/style.css")
				(link 'rel "stylesheet" 'href "https://fonts.googleapis.com/css?family=Josefin+Sans&display=swap")
				(link 'rel "stylesheet" 'href "https://fonts.googleapis.com/css?family=Open+Sans&display=swap")
				(link 'rel "stylesheet" 'href "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css")
				(link 'rel "stylesheet" 'href "/js/lightbox/dist/css/lightbox.min.css")
				(script 'src "/js/lightbox/dist/js/lightbox-plus-jquery.min.js"))
			(body 
				(con 
					fklub-header
					(div 'class "content" 
						x)
					fklub-footer)))))

(define (repeat-el x el)
	(if (<= x 1) el
		(con el (repeat (- x 1) el))))

(define (bare-page page-title x) 
	(cgi-write 
		(html
			(head
				(title (string-append page-title " - Fklub.dk"))
				(meta 'charset "utf-8")
				(link 'rel "stylesheet" 'href "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css")
				(link 'rel "stylesheet" 'href "/style.css")
				(link 'rel "stylesheet" 'href "https://fonts.googleapis.com/css?family=Josefin+Sans&display=swap")
				(link 'rel "stylesheet" 'href "https://fonts.googleapis.com/css?family=Open+Sans&display=swap")
				(link 'rel "stylesheet" 'href "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"))
			(body x))))

(define (input-text name placeholder)
	(input 'type "text" 'placeholder placeholder 'name name 'class "form-control"))

(define (submit-btn value)
	(input 'type "submit" 'class "btn btn-primary" 'value value))