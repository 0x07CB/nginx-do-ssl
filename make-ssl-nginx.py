#coding: utf-8
import os
domain_name = input("domain_name: ")
# =====================================
os.system("sudo echo OK")
data="""
sudo mkdir -p /var/www/{}/html
sudo chown -R $USER:$USER /var/www/{}/html
sudo chmod -R 755 /var/www/{}
""".format(domain_name,domain_name,domain_name)
os.system(data)
# =====================================
f=open("/var/www/{}/html/index.html".format(domain_name),'w')
data = """
<html>
    <head>
        <title>Welcome to {}</title>
    </head>
    <body>
        <h1>Success! Your Nginx server is successfully configured for <em>{}</em>. </h1>
<p>This is a sample page.</p>
    </body>
</html>
""".format(domain_name,domain_name)
f.write(data)
f.close()
# =====================================
f=open("/etc/nginx/sites-available/{}".format(domain_name),'w')
data = """
server {
        listen 80;
        listen [::]:80;

        root /var/www/"""+domain_name+""""/html;
        index index.html index.htm index.nginx-debian.html;

        server_name """+domain_name+""" www."""+domain_name+""";

        location / {
                try_files $uri $uri/ =404;
        }
}
"""
f.write(data)
f.close()
os.system("sudo ln -s /etc/nginx/sites-available/{} /etc/nginx/sites-enabled/".format(domain_name))
f=open("/etc/nginx/nginx.conf",'r')
data=f.read()
f.close()
if data.count("#server_names_hash_bucket_size 64;"):
	data = data.replace("#server_names_hash_bucket_size 64;","server_names_hash_bucket_size 64;")
	f=open("/etc/nginx/nginx.conf",'w')
	f.write(data)
	f.close()
os.system("sudo nginx -t")
os.system("sudo nginx -s stop")
os.system("sudo nginx -")
os.system("sudo certbot --nginx -d {}".format(domain_name))
print("DONE.")