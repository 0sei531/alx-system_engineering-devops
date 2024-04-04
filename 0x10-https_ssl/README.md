MAWK(1)                                                         USER COMMANDS                                                        MAWK(1)

NAME
       mawk - pattern scanning and text processing language

SYNOPSIS
       mawk [-W option] [-F value] [-v var=value] [--] 'program text' [file ...]
       mawk [-W option] [-F value] [-v var=value] [-f program-file] [--] [file ...]

DESCRIPTION
       mawk  is  an interpreter for the AWK Programming Language.  The AWK language is useful for manipulation of data files, text retrieval
       and processing, and for prototyping and experimenting with algorithms.  mawk is a new awk meaning it implements the AWK  language  as
       defined in Aho, Kernighan and Weinberger, The AWK Programming Language, Addison-Wesley Publishing, 1988 (hereafter referred to as the
       AWK book.)  mawk conforms to the POSIX 1003.2 (draft 11.3) definition of the AWK language which contains a few features not described
       in the AWK book, and mawk provides a small number of extensions.

       An AWK program is a sequence of pattern {action} pairs and function definitions.  Short programs are entered on the command line usu‐
       ally enclosed in ' ' to avoid shell interpretation.  Longer programs can be read in from a file with the -f option.  Data   input  is
       read  from  the list of files on the command line or from standard input when the list is empty.  The input is broken into records as
       determined by the record separator variable, RS.  Initially, RS = “\n” and records are synonymous with lines.  Each  record  is  com‐
       pared against each pattern and if it matches, the program text for {action} is executed.

OPTIONS
       -F value       sets the field separator, FS, to value.

       -f file        Program text is read from file instead of from the command line.  Multiple -f options are allowed.

       -v var=value   assigns value to program variable var.

       --             indicates the unambiguous end of options.

       The  above  options  will be available with any POSIX compatible implementation of AWK.  Implementation specific options are prefaced
       with -W.  mawk provides these:

       -W dump        writes an assembler like listing of the internal representation of the program to stdout and exits  0  (on  successful
                      compilation).

DIG(1)                                                              BIND9                                                             DIG(1)

NAME
       dig - DNS lookup utility

SYNOPSIS
       dig [@server] [-b address] [-c class] [-f filename] [-k filename] [-m] [-p port#] [-q name] [-t type] [-v] [-x addr]
           [-y [hmac:]name:key] [[-4] | [-6]] [name] [type] [class] [queryopt...]

       dig [-h]

       dig [global-queryopt...] [query...]

DESCRIPTION
       dig is a flexible tool for interrogating DNS name servers. It performs DNS lookups and displays the answers that are returned from
       the name server(s) that were queried. Most DNS administrators use dig to troubleshoot DNS problems because of its flexibility, ease
       of use and clarity of output. Other lookup tools tend to have less functionality than dig.

       Although dig is normally used with command-line arguments, it also has a batch mode of operation for reading lookup requests from a
       file. A brief summary of its command-line arguments and options is printed when the -h option is given. Unlike earlier versions, the
       BIND 9 implementation of dig allows multiple lookups to be issued from the command line.

       Unless it is told to query a specific name server, dig will try each of the servers listed in /etc/resolv.conf. If no usable server
       addresses are found, dig will send the query to the local host.

       When no command line arguments or options are given, dig will perform an NS query for "." (the root).

       It is possible to set per-user defaults for dig via ${HOME}/.digrc. This file is read and any options in it are applied before the
       command line arguments. The -r option disables this feature, for scripts that need predictable behaviour.

       The IN and CH class names overlap with the IN and CH top level domain names. Either use the -t and -c options to specify the type and
       class, use the -q the specify the domain name, or use "IN." and "CH." when looking up these top level domains.

