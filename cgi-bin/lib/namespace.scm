(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")
(cgi-lib-load "lib/common.scm")

; Utility functions allowed in markup language

(define (f-section color . data)
        (div 'class "section" 
            'style (string-append "background-color:" color ";") 
            (container (con data))))

(define (f-img url)
    (div 'class "imagecontainer" (img 'src url)))

(define (f-youtube url)
    (div 'class "imagecontainer" (iframe 'width 560 'height 315 'src (string-append "https://www.youtube.com/embed/" url) 'frameborder "0" 'allow "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 'allowfullscreen "")))

(define (f-imgs . data)
    (div 'class "imagescontainer" (con data)))

(define (f-link url . data)
    (a 'href url (con data)))

(define (f-link-image url image-url)
    (a 'href url (img 'src image-url 'class "image-link")))

(define (f-button-primary url . data)
    (a 'class "btn btn-primary" 'href url (con data)))

(define (f-button-secondary url . data)
    (a 'class "btn btn-secondary" 'href url (con data)))

(define (f-button-info url . data)
    (a 'class "btn btn-info" 'href url (con data)))

(define (f-center . data) 
    (div 'class "center" (con data)))

(define create-famespace
  (lambda ()
    (let ((ns (make-namespace))) 
        (parameterize ((current-namespace ns)) 
          (begin 
            (namespace-set-variable-value! 'section f-section)
            (namespace-set-variable-value! 'text p)
            (namespace-set-variable-value! 'image f-img)
            (namespace-set-variable-value! 'youtube f-youtube)
            (namespace-set-variable-value! 'images f-imgs)
            (namespace-set-variable-value! 'title h2)
            (namespace-set-variable-value! 'link f-link)
            (namespace-set-variable-value! 'imagelink f-link-image)
            (namespace-set-variable-value! 'button-primary f-button-primary)
            (namespace-set-variable-value! 'button-secondary f-button-secondary)
            (namespace-set-variable-value! 'button-info f-button-info)
            (namespace-set-variable-value! 'center f-center)
            (namespace-set-variable-value! 'bold b)
            ns)))))



