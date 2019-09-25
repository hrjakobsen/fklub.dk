#!/usr/bin/plt/bin/mzscheme -r

(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  
(lib-load "color.scm") ;  

; HTML mirror loading
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")


(load "/usr/local/cgi-bin/lib/common.scm")
(cgi-lib-load "admin/admin.scm")
(cgi-lib-load "common.scm")
(cgi-lib-load "lib/file.scm")
(cgi-lib-load "lib/utf-8-form-fix.scm")

(ensure-admin)

(define cgi-testing #f)

(let* ((form-a-list (map symbolize-key (extract-form-input))) ;  
    (data (as-string (get 'data form-a-list)))
   )
(begin 
	(write-data-file "/data/frontpage.scm" data)
	(redirect "/cgi-bin/admin/edit-frontpage.cgi")
)
)



(end)
