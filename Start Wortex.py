import wordlist
import time
import sys
import os


while(True):
 banner1 = """
                                                   \033[1;34m.
                                                  \033[1;34m/ \      _-'|
                                               \033[1;34m._/|  \-''- _ /
   \033[1;31m__          __        _                 \033[1;34m__-' { |          \.
   \033[1;31m\ \	      / /       | |                    \033[1;34m/              \.
    \033[1;31m\ \  /\  / /__  _ __| |_ _____  __        \033[1;34m/       "o.  |o }
     \033[1;31m\ \/  \/ / _ \| '__| __/ _ \ \/ /        \033[1;34m|            \  ;
      \033[1;31m\  /\  / ( ) | |  | ||  __/>  <           \033[1;34m.           ',
       \033[1;31m\/  \/ \___/|_|   \__\___/_/\_\           \033[1;34m\_         __\.
       \033[1;31m_______________________________             \033[1;34m''-_    \.//
          </>   TGT Wordlist Generator               \033[1;34m/ '-____'
                                                    \033[1;34m/
                                                  \033[1;34m_'
                                               \033[1;34m_-'                                                                                                                                                                                                              
 """

 banner2 = """
                           \033[0m|^^^^^^^^^^^^^^^^^^^^^^^^^^|
 __________________________|\033[0m> \033[1;34mTGT Wordlist Generator \033[0m<|_________________________                                             
/>                            \033[0m< \033[1;31mMade By Wr4th#0001 \033[0m>       \033[1;31m__          __     \033[0m* <\.
|>    Version: 1.0             \033[0m> \033[1;31mTurkish Guy Tim \033[0m<        \033[1;31m\ \        / /     \033[0m* <|               
|>                                 \033[0m< \033[1;34mWortex \033[0m>              \033[1;31m\ \  /\  / /      \033[0m* <|
|>                                                          \033[1;31m\ \/  \/ /       \033[0m* <|
|> \033[1;32mBu Tool Ki??iye ??zel Wordlist Olu??turur!                   \033[1;31m\  /\  /        \033[0m* <|
|> \033[1;32mSocial Medias / Sosyal Medyalar;                           \033[1;31m\/  \/         \033[0m* <|
|> \033[1;31mYoutube: https://www.youtube.com/channel/UCXspb19nmlqMkuakJklcqsw         \033[0m* <|
|> \033[1;34mDiscord: https://discord.gg/eZKQWcmuNy                                    \033[0m* <|
|> \033[0mWebSite: http://turkishguyteam.rf.gd/ \033[1;31m00110011 \033[1;32m00110001 \033[1;33m01110011 \033[1;34m01101010 \033[0m* <|                                                                                                 
\_______________________________________________________________________________/
 """

 banner3 = """
______________________________________________________________________
| \033[1;34mWortex TGT Wordlist Generator                                      \033[0m| 
| \033[1;31m[1] Wordlist Olu??tur / Create Wordlist                             \033[0m|
| \033[1;32m[2] Gereksinimleri Y??kle / Install Requirments                     \033[0m|
| \033[1;33m[3] Sosyal Medya / Social Media  \033[0;31m                 [4] ????k????/Exit   \033[0m|
|____________________________________________________________________|
 """
 banner4 = """
_________________________________________________________________________________
|\033[1;31m Youtube: https://www.youtube.com/channel/UCXspb19nmlqMkuakJklcqsw              \033[0m|
|\033[1;34m Discord: https://discord.gg/eZKQWcmuNy                                         \033[0m|    
|\033[0m WebSite: http://turkishguyteam.rf.gd/                                          |
|________________________________________________________________________________|
 """

 print(banner1)
 print(banner2)

 input("\033[0;32m [>] \033[1;34mWortex Wordlist Generator \033[0m| Devam Etmek ????in Enter'a Bas??n??z...")

 print(banner3)

 islem = input("\033[0;34m[#] \033[0mL??tfen ????lem Se??iniz >")


 if islem == "4":
    break
    sys.exit()

 elif islem == "3":
      print(banner4)
      input("\033[0;32m [>] \033[1;34mAna Menu \033[0m| Devam Etmek ????in Enter'a Bas??n??z...")
      pass


 elif islem == "2":
      print("__________________________________")
      grksnmsoru = input("\033[0;34m[?] \033[0mGereksinimler Y??klensinmi? [\033[0;32mY\033[0m/\033[0;31mn\033[0m] >")

      if grksnmsoru == "Y" or grksnmsoru == "y":
            print("\033[0;32m[%] \033[0mGereksinimler Y??kleniyor L??tfen Bekleyin..")
            time.sleep(1)
            os.system("pip install wordlist")
            print(" ===========================================================================")
            input("\033[0;32m[>] \033[1;34mAna Menu \033[0m| ????lem Tamamland??! Devam Etmek ????in Enter'a Bas??n??z...")
            pass

      elif grksnmsoru == "N" or grksnmsoru == "n":
          input("\033[0;32m[>] \033[1;34mAna Menu \033[0m| Devam Etmek ????in Enter'a Bas??n??z...")
          pass



 elif islem == "1":
     print("______________________________________")
     min = int(input("\033[0;34m[#] \033[0mMinumum ??ifre Uzunlu??unu Giriniz >"))
     max = int(input("\033[0;34m[#] \033[0mMaksimum ??ifre Uzunlu??unu Giriniz >"))
     print("______________________________________")
     print("\033[0;31m??rn: \033[0m??sim, Do??um Tarihi, ????inde Bulumas??n?? ??stedi??iniz Karakterler. \033[0;31m??rn: \033[0mqwerty12345")
     bilgi = input("\033[0;34m[#] \033[0mKurban Hakk??nda Bilgi Girin >")

     wordlistname = input("\033[0;34m[#] \033[0mWordlist ??smi Giriniz >")

     onay = input("\033[0;34m[?] \033[0mWordlist Olu??turulsunmu? [\033[0;32mY\033[0m/\033[0;31mn\033[0m] >")
     if onay == "Y" or onay == "y":
         pass

     elif onay == "N" or onay == "n":
         input("\033[0;32m[>] \033[1;34mAna Menu \033[0m| Devam Etmek ????in Enter'a Bas??n??z...")
         pass

     else:
         input("\033[0;31m[!] \033[0mHata! L??tfen Do??ru Yaz??????n??zdan Emin Olun! | Devam Etmek ????in Enter'a Bas??n??z...")
         pass

     generate = wordlist.Generator(bilgi)


 try:
     with open(wordlistname + ".txt", "a") as wordlist1:
         toplamkelime = 0
         for i in generate.generate(min,max):
              wordlist1.write(i)
              wordlist1.write("\n")
              toplamkelime += 1
         print("____________________________________________________________________________________________")
         print("\033[0;32m[%] \033[0mWordlist Yaz??l??yor, L??tfen Bekleyin... Bu S??re ??ifrelerin Uzunlu??una G??re De??i??ebilir...")
         time.sleep(15)
         print("\033[0;32m[/] ????lem Tamamland??! \033[0mOlu??turulan Kelime Say??s?? = (\033[0;31m"+str(toplamkelime)+"\033[0m)")
         input("\033[0;32m[>] \033[1;34mAna Menu \033[0m| Devam Etmek ????in Enter'a Bas??n??z...")
         pass

 except ValueError:
     input("\033[0;31m[!] \033[0mHata! L??tfen D??zg??n De??erler Girdi??inizden Emin Olun! | Devam Etmek ????in Enter'a Bas??n??z...")
     pass





