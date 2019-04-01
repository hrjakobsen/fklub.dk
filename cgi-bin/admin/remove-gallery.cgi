#!/usr/bin/plt/bin/mzscheme -r

(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  
(lib-load "color.scm") ;  
(lib-load "collect-skip.scm") ;  
(lib-load "file-read.scm") ;  

; HTML mirror loading
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")

(load "/usr/local/cgi-bin/lib/common.scm")
(cgi-lib-load "admin/admin.scm")
(cgi-lib-load "common.scm")
(cgi-lib-load "lib/file.scm")

(ensure-admin)

(define cgi-testing #f)

(define url-pars (extract-url-parameters))

(define cur-gallery 
	(as-symbol (defaulted-get 'cur-gallery url-pars 'qawsdgfhjklnbhgdcfgkhjk ))) ; invalid gallery so the scripts fails


(delete-directory (string-append "/data/galleries/" (symbol->string cur-gallery)))

(redirect "/cgi-bin/admin/edit-gallery.cgi")

(end)
