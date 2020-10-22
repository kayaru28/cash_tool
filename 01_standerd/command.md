# Setting

## Apache PHP
yum -y install httpd
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
yum -y install --enablerepo=remi,remi-php56 php php-devel php-mbstring php-pdo php-gd

## activate
systemctl start httpd
systemctl enable httpd
systemctl restart httpd

## setting back up
cd /etc/httpd/conf/
cp httpd.conf httpd.conf.org

## security
firewall-cmd --permanent --add-service=http
firewall-cmd --reload

## root dir
cd /var/www/html

