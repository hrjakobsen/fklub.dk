; In order to handle passwords as safely as possible
; we include the libcrypt.so shared library, which is compiled
; from https://www.openwall.com/crypt/ and placed in the public 
; domain. We use the foreign.ss scheme module to interface with 
; the C library. This allows us to use bcrypt as the hashing 
; algorithm, instead of the insecure default LAML "hashing".  

(require (lib "foreign.ss")) (unsafe!)


; We make use of the two functions crypt_gensalt_ra and crypt_ra
; from the library, to generate a salt for bcrypt, and do the 
; hashing respectively. 
(define crypt_ra
  (get-ffi-obj 'crypt_ra "/usr/local/cgi-bin/lib/libcrypt.so"
				(_fun (key settings data size) :: (key : _u8vector) (settings : _u8vector) (data : (_ptr o _u8vector)) (size : (_ptr i _int)) -> _u8vector)
				(lambda ()
					(error 'libtest
						"installed libcrypt does not provide \"crypt_ra\" which is needed to perform password hashing"))))

(define crypt_gensalt_ra
  (get-ffi-obj 'crypt_gensalt_ra "/usr/local/cgi-bin/lib/libcrypt.so"
				(_fun (prefix count input size) :: (prefix : _u8vector) (count : _long) (input : _u8vector) (size : _int) -> _u8vector)
				(lambda ()
					(error 'libtest
						"installed libcrypt does not provide \"crypt_gensalt_ra\" which is needed to perform password hashing"))))

(define (entropy size) (list->string (entropy-int size)))

(define (entropy-int size) 
  (if (< size 1) 
	  '()
	  (cons (integer->char (random 255)) (entropy-int (- size 1)))))

; Wrappers around the crypt functions make conversions
; between strings and bytevectors
(define (generate-salt cost)
	(crypt_gensalt_ra (string->bytes/utf-8 "$2b$") cost (string->bytes/utf-8 (entropy 16)) 16))

(define (hash-password-default pw) 
	(hash-password pw (generate-salt 12)))

(define (hash-password pw settings) 
	(bytes->string/utf-8 (crypt_ra (string->bytes/utf-8 pw) settings (make-bytes 0) 0)))


; To validate the passwords, we extract the 'settings' string
; containing the algorithm (always "2b"), the cost and the salt.
; We then hash the password to check using these settings, and 
; compare the result with the hashed password we stored previously.
(define bcrypt-pattern (regexp "\\$2b\\$([0-9]+)\\$([a-zA-Z0-9\\./]+)"))

(define (extract-settings hash)
	(let ((matches (regexp-match bcrypt-pattern hash)))
		(if (equal? matches #f)
			#f
			(let ((cost (cadr matches))
				  (rem (caddr matches)))
				  (if (= (string-length rem) 53)
				  	(string-append "$2b$" cost "$" (substring rem 0 22))
					#f)))))


(define (validate-password pw hash)
	(let ((settings (extract-settings hash)))
		 (if (equal? #f settings) #f
			(equal? (hash-password pw (string->bytes/utf-8 settings)) hash))))
