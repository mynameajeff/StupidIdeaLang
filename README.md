# StupidIdeaLang
This is an esoteric language I had the idea for in only 2 minutes, and spent the next 8 or so hours implementing.

SYNTAX EXPLANATION OF NEW BACKWARDS LANGUAGE:

    : - BEGIN

    s - STACK

    (?)<s - MOVE (?) TO THE STACK
        NOTE: (?) MUST BE A STRING

    ' - DENOTE BEGINNING OF A STRING
    " - DENOTE END OF A STRING

    ; - DENOTE END OF STATEMENT, AND BEGINNING OF NEXT STATEMENT

    (?)/(??) - POP FROM (??), AND PUSH TO (?)
    s/, - GET INPUT DATA FROM THE STDIN, AND STORE IN THE STACK
    ./s - GET DATA FROM THE STACK, AND STORE IN THE STDOUT

    . - STDOUT
    , - STDIN

    \n - NEWLINE
    \' - '
