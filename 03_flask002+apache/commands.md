# setup
yum install mod_wsgi





また、Apache の設定ファイルの一部も書き換えます。(.conf ファイル)

LoadModule wsgi_module modules/mod_wsgi.so

<VirtualHost *:80>
    ServerName wsgiapp.example.com

    WSGIDaemonProcess flask-wsgi user=apache group=apache threads=5
    WSGIScriptAlias / /var/www/html/wsgi/connector.wsgi

    WSGIScriptReloading On

    <Directory "/var/www/html/wsgi">
        WSGIProcessGroup flask-wsgi
        WSGIApplicationGroup %{GLOBAL}
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>