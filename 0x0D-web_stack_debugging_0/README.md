AME
       curl - transfer a URL

SYNOPSIS
       curl [options / URLs]

DESCRIPTION
       curl  is  a  tool  to  transfer  data from or to a server, using one of the supported protocols (DICT, FILE, FTP, FTPS, GOPHER, HTTP,
       HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET and TFTP).  The  command  is  de‐
       signed to work without user interaction.

       curl offers a busload of useful tricks like proxy support, user authentication, FTP upload, HTTP post, SSL connections, cookies, file
       transfer resume, Metalink, and more. As you will see below, the number of features will make your head spin!

       curl is powered by libcurl for all transfer-related features. See libcurl(3) for details.

URL
       The URL syntax is protocol-dependent. You'll find a detailed description in RFC 3986.

       You can specify multiple URLs or parts of URLs by writing part sets within braces as in:

         http://site.{one,two,three}.com

       or you can get sequences of alphanumeric series by using [] as in:

         ftp://ftp.example.com/file[1-100].txt

         ftp://ftp.example.com/file[001-100].txt    (with leading zeros)

         ftp://ftp.example.com/file[a-z].txt

       Nested sequences are not supported, but you can use several ones next to each other:

         http://example.com/archive[1996-1999]/vol[1-4]/part{a,b,c}.html

       You can specify any amount of URLs on the command line. They will be fetched in a sequential manner in the specified order.  You  can
       specify command line options and URLs mixed and in any order on the command line.

       You can specify a step counter for the ranges to get every Nth number or letter:

         http://example.com/file[1-100:10].txt

         http://example.com/file[a-z:2].txt

       When  using [] or {} sequences when invoked from a command line prompt, you probably have to put the full URL within double quotes to
       avoid the shell from interfering with it. This also goes for other characters treated special, like for example '&', '?' and '*'.

       Provide the IPv6 zone index in the URL with an escaped percentage sign and the interface name. Like in

         http://[fe80::3%25eth0]/

       If you specify URL without protocol:// prefix, curl will attempt to guess what protocol you might want. It will then default to  HTTP
       but try other protocols based on often-used host name prefixes. For example, for host names starting with "ftp." curl will assume you
       want to speak FTP.

       curl will do its best to use what you pass to it as a URL. It is not trying to validate it as a  syntactically  correct  URL  by  any
       means but is instead very liberal with what it accepts.

       curl will attempt to re-use connections for multiple file transfers, so that getting many files from the same server will not do mul‐
       tiple connects / handshakes. This improves speed. Of course this is only done on files specified on a single command line and  cannot
       be used between separate curl invokes.

PROGRESS METER
       curl  normally  displays a progress meter during operations, indicating the amount of transferred data, transfer speeds and estimated
       time left, etc. The progress meter displays number of bytes and the speeds are in bytes per second. The suffixes (k, M, G, T, P)  are
       1024 based. For example 1k is 1024 bytes. 1M is 1048576 bytes.

