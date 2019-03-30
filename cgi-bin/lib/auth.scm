(define (admin? username session-id)
    (and 
        (string? username) 
        (string? session-id)
        (correct-session? username session-id)))


(define (correct-session? username session)
    (let* 
        ((data (read-data-file (string-append "/data/users/" username "/session.dat"))))
        (equal? data session)))