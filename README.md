# SSL-NGINX-AUTO_COMPLETE-NEXTS

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/667fdf0db8f542528be92105a022af4a)](https://www.codacy.com?utm_source=gitlab.com&amp;utm_medium=referral&amp;utm_content=LaGvidilo/ssl-nginx-auto_complete-nexts&amp;utm_campaign=Badge_Grade)

auto complete the SSL validation and server blocks creation and configuration for validation

# SOURCE OF INSPIRATION
how-to-install-nginx-on-debian-10: [digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-debian-10)

mongodb-ssl-setup: [jamesloper.com](https://jamesloper.com/mongodb-ssl-setup)

# REQUIREMENT
1.  install certbot & nginx
    (if you are under Ubuntu)
    ```
    sudo add-apt-repository ppa:certbot/certbot
    sudo add-apt-repository ppa:nginx/stable
    ```

    (IN ALL CASE INSTALL THAT)
    ```
    sudo apt update && sudo apt install -y software-properties-common python-certbot-nginx && sudo apt install -y nginx
    ```
2.  upgrade and reboot
    **NOTE: SAVE ALL WORK OPEN BECAUSE YOU NEED TO REBOOT**
    ```
    sudo apt update && sudo apt upgrade -y 
    sudo reboot
    ```

3.  Setting up an firewall(regular and minimal configuration follow this)
    - INSTALL UFW
    `sudo apt update && sudo apt install -y ufw`
    
    - look the list of applications of UFW detect for configure
    `sudo ufw app list`
    _**For this moment don't touch another things if is not in this documentation or you aren't an senior in cybersécurity**_
    _**AND PLEASE DON'T PUT OUT OF YOU, YOUR ACCESS (if is distant) CAN BE DENY IF YOU SET AN DENY ON OpenSSH service or the 22 port, SO PLEASE DO NOT THAT IF YOU ARE NOT PHYSICALY IN ACCESS WITH KEYBOARD OF THE SERVER !!!!**_

    - ALLOW HTTP AND HTTPS OF NGINX
    ```
    sudo ufw allow 'Nginx HTTP'
    sudo ufw allow 'Nginx HTTPS'
    ```
    
    - DISABLE && ENABLE UFW && VERIFY UFW STATUS
    ```
    sudo ufw reload
    sudo ufw status
    ```
    Additional status infos:
    ```
    sudo systemctl status nginx
    ```

4.  LOOK YOUR IP ADDRESS & CONFIGURE REDIRECTION OF DOMAIN NAME
    `ip addr show eth0 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//'`

    or just that with hostname command

    `sudo hostname -I`

    **_YOU NEED TO CONFIGURE AN REDIRECTION OF TYPE (A) BETWEEN THE DOMAIN NAME AND THE IP OF YOUR SERVER_**

5.  BE SURE NGINX AND UFW IT'S OKAY
    - STOP NGINX AND UFW
    `sudo ufw disable && sudo nginx -s stop`

    - RELAUCH NGINX AND UFW
    `sudo ufw enable && sudo nginx -`

    (YOU CAN VERIFY IF YOU HAVE A TROUBLES THE STATUS OF NGINX VALIDITY AND UFW RULES)
    `sudo ufw status && sudo ufw app list && sudo nginx -t`

6.  FINALLY RUN THE SCRIPT
    **NOTE: SAVE ALL WORK OPEN BECAUSE YOU NEED TO REBOOT**
    PLACE YOU INTO THE FOLDER OF THE SCRIPT
    AND LAUNCH THE SCRIPT WITH PYTHON3 (THE SCRIPT ASK YOU ONLY THE DOMAIN NAME AND LET'S GO)
    AND PLEASE MAKE BY SECURITY UPDATE & UPGRADE & REBOOT : (dont forgot the step 7)
    **AND DON'T FORGOT TO RESET IN HARD MODE YOUR REPOSITORY FOLDER**
    ```
    sudo python3 make-ssl-nginx.py
    sudo git reset --hard HEAD
    sudo update && sudo upgrade -y && sudo reboot
    ```

**_ It's DONE ! Hoooooo yeah ! _**

# =====================================
_RICK SANCHEZ_
