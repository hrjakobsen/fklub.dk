(cgi-lib-load "lib/cgi.scm")
(cgi-lib-load "lib/cookies.scm")
(cgi-lib-load "lib/auth.scm")
(cgi-lib-load "lib/convenience.scm")
(cgi-lib-load "lib/common.scm")
(cgi-lib-load "common.scm")

(define ensure-admin (lambda ()
    (if (admin? (get-cookie 'username ) (get-cookie 'session-id )) 
        #t
        (begin 
            (redirect "/cgi-bin/login.cgi") 
            (end))
        )))

(define admin-menu `(
    ("Rediger FAQ" . "/cgi-bin/admin/edit-faq.cgi")
    ("Rediger Galleri" . "/cgi-bin/admin/edit-gallery.cgi")
    ("Rediger F-ordbog" . "/cgi-bin/admin/edit-f-ordbog.cgi")
    ("Rediger Forside" . "/cgi-bin/admin/edit-frontpage.cgi")
    (,(fa "sign-out") . "/cgi-bin/logout.cgi")
    ))

(define menu-list 
	(map (lambda (x) (div 'class "col" (a 'class "menu-link" 'href (cdr x) (car x)))) admin-menu))


(define admin-menu-list 
	(div 'class "header" 
			(container
				(div 'class "menu"
					(row (con menu-list))))))