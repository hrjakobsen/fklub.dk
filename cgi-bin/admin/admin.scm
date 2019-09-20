(cgi-lib-load "lib/cgi.scm")
(cgi-lib-load "lib/cookies.scm")
(cgi-lib-load "lib/auth.scm")

(define ensure-admin (lambda ()
    (if (admin? (get-cookie 'username ) (get-cookie 'session-id )) 
        #t
        (begin 
            (redirect "/cgi-bin/login.cgi") 
            (end))
        )))

(define admin-menu '(
    ("Rediger FAQ" . "/cgi-bin/admin/edit-faq.cgi")
    ("Rediger Galleri" . "/cgi-bin/admin/edit-gallery.cgi")
    ("Rediger F-ordbog" . "/cgi-bin/admin/edit-f-ordbog.cgi")
    ("Log ud" . "/cgi-bin/logout.cgi")
    ))

(define admin-menu-list 
    (ul
        (map (lambda (x) (li (a 'href (cdr x) (car x)))) admin-menu)
    ))
