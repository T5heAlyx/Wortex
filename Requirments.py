import os
import time

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

print(banner1)
print("\033[0;31m________________________________________________________________\n")
grksnmsoru = input("\033[0;34m[?] \033[0mGereksinimler Yüklensinmi? [\033[0;32mY\033[0m/\033[0;31mn\033[0m] >")

if grksnmsoru == "Y" or grksnmsoru == "y":
            print("\033[0;32m[%] \033[0mGereksinimler Yükleniyor Lütfen Bekleyin..")
            time.sleep(1)
            os.system("pip install wordlist")
            print(" ===========================================================================")
            input("\033[0;32m[>] \033[0mİşlem Tamamlandı! Devam Etmek İçin Enter'a Basınız...")