NAME
     scp — OpenSSH secure file copy

SYNOPSIS
     scp [-346BCpqrTv] [-c cipher] [-F ssh_config] [-i identity_file] [-J destination] [-l limit] [-o ssh_option] [-P port] [-S program]
         source ... target

DESCRIPTION
     scp copies files between hosts on a network.  It uses ssh(1) for data transfer, and uses the same authentication and provides the same
     security as ssh(1).  scp will ask for passwords or passphrases if they are needed for authentication.

     The source and target may be specified as a local pathname, a remote host with optional path in the form [user@]host:[path], or a URI
     in the form scp://[user@]host[:port][/path].  Local file names can be made explicit using absolute or relative pathnames to avoid scp
     treating file names containing ‘:’ as host specifiers.

     When copying between two remote hosts, if the URI format is used, a port may only be specified on the target if the -3 option is used.

     The options are as follows:

     -3      Copies between two remote hosts are transferred through the local host.  Without this option the data is copied directly be‐
             tween the two remote hosts.  Note that this option disables the progress meter.

     -4      Forces scp to use IPv4 addresses only.

     -6      Forces scp to use IPv6 addresses only.

     -B      Selects batch mode (prevents asking for passwords or passphrases).

     -C      Compression enable.  Passes the -C flag to ssh(1) to enable compression.

     -c cipher
             Selects the cipher to use for encrypting the data transfer.  This option is directly passed to ssh(1).

 Manual page scp(1) line 1 (press h for help or q

NAME
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
