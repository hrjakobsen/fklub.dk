#!/usr/bin/plt/bin/mzscheme -r

(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  

; HTML mirror loading
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")

(load "common.scm")
(define cgi-testing #f)

(fklub-page
  "test"
  (container
  	(iframe 'src "https://calendar.google.com/calendar/embed?showPrint=0&amp;showTabs=0&amp;showCalendars=0&amp;height=600&amp;wkst=2&amp;bgcolor=%23FFFFFF&amp;src=fke9k8sbuqttoif5ff7ccbb0bc%40group.calendar.google.com&amp;color=%232F6309&amp;ctz=Europe%2FAmsterdam"
  	'style "border-width:0" 'width "100%" 'height "600" 'frameborder "0" 'scolling "no")
  ))


(end)

