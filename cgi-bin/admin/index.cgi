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
(cgi-lib-load "lib/cookies.scm")

(ensure-admin)

(fklub-page
  "Admin forside"
  (con 
    admin-menu-list
    (container (con 
      (h2 (string-append "Velkommen, " (get-cookie 'username ) "!"))
      (p "Det er her det sjove sker. Her kan du finjustere indholdet på fklub.dk. Er der kommet et nyt spørgsmål? Ret FAQ'en. Nyt arrangement? Opret et galleri. Nyt fordspil? Tilføj det til F-ordbogen. Sidst men ikke mindst har du mulighed for at fremvise dine Scheme evner, ved at opdatere forsiden, som selvfølgelig skrives i vores alle sammen yndlingssprog. ")))
    )
)

(end)
