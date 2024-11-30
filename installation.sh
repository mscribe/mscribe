#!/bin/bash




# Icon:
echo "······················································";
echo ":                                                    :";
echo ":                                                    :";
echo ":                                                    :";
echo ":    ___      ___  ___        ______    _______      :";
echo ":   |\"  \    /\"  ||\"  |      /    \" \  /\" _   \"|     :";
echo ":    \   \  //   |||  |     // ____  \(: ( \___)     :";
echo ":    /\\  \/.    ||:  |    /  /    ) :)\/ \           :";
echo ":   |: \.        | \  |___(: (____/ // //  \ ___     :";
echo ":   |.  \    /:  |( \_|:  \\        / (:   _(  _|     :";
echo ":   |___|\__/|___| \_______)\"_____/   \_______)      :";
echo ":                                                    :";
echo ":                                                    :";
echo ":                                                    :";
echo ":                                                    :";
echo "······················································";


# General Information
VERSION=$(grep -Eroh 'v[0-9]+\.[0-9]+\.[0-9]+' ../src 2>/dev/null)
echo "MLOG $VERSION Installation"


# Variables
SRC_PATH=./src
IP=$(hostname -I | awk '{print $1}')


# Database Credentials
echo "MySQL Database Credentials"

read -p "Enter database host [default: localhost]: " database_host
database_host=${database_host:-localhost}

read -p "Enter database user [default: blog]: " database_user
database_user=${database_user:-blog}

read -sp "Enter database password: " database_password
echo

read -p "Enter database schema [default: blog]: " database_schema
database_schema=${database_schema:-blog}

read -p "Enter database port [default: 3306]: " database_port
database_port=${database_port:-3306}


# Installation
echo "Updating and upgrading the system..."
sudo apt update && sudo apt upgrade -y

echo "Installing required packages..."
sudo apt install -y python3-pip python3-dev libmysqlclient-dev

if [[ "$database_host" == "localhost" ]]; then
    echo "Installing MySQL server..."
    sudo apt install -y mysql-server
    echo "Securing MySQL installation..."
    sudo mysql_secure_installation
else
    echo "Skipping MySQL server installation since database host is not localhost."
fi

echo "Creating database and user..."
sudo mysql -e "CREATE DATABASE IF NOT EXISTS \`$database_schema\`;"
sudo mysql -e "CREATE USER IF NOT EXISTS '$database_user'@'localhost' IDENTIFIED BY '$database_password';"
sudo mysql -e "GRANT ALL PRIVILEGES ON \`$database_schema\`.* TO '$database_user'@'$database_host';"
sudo mysql -e "FLUSH PRIVILEGES;"

echo "Installing Apache and mod_wsgi..."
sudo apt install -y apache2 libapache2-mod-wsgi-py3

echo "Installing Python 3.11..."
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install -y python3.11 python3.11-venv python3.11-dev
echo "Installation completed successfully!"


# Configuration
WSGI_FILE="$SRC_PATH/myflaskapp.wsgi"
echo "Creating WSGI file at $WSGI_FILE..."

cat <<EOL > $WSGI_FILE
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from website import create_website
application = create_website()
EOL

APACHE_CONF="/etc/apache2/sites-available/myflaskapp.conf"
echo "Creating Apache configuration file at $APACHE_CONF..."

cat <<EOL | sudo tee $APACHE_CONF
<VirtualHost *:80>
    ServerName $IP
    Redirect permanent / https://$IP/
</VirtualHost>

<VirtualHost *:443>
    ServerName $IP

    WSGIDaemonProcess myflaskapp python-home=/usr/bin/python3 python-path=$SRC_PATH
    WSGIProcessGroup myflaskapp

    WSGIScriptAlias / $WSGI_FILE

    <Directory $SRC_PATH>
        Require all granted
    </Directory>

    ErrorLog \${APACHE_LOG_DIR}/myflaskapp_error.log
    CustomLog \${APACHE_LOG_DIR}/myflaskapp_access.log combined

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/your_domain_or_IP/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/your_domain_or_IP/privkey.pem
</VirtualHost>
EOL

echo "Enabling the new site and SSL module..."
sudo a2ensite myflaskapp
sudo a2enmod ssl
sudo systemctl restart apache2

echo "Installing Certbot and obtaining SSL certificate..."
sudo apt install -y certbot python3-certbot-apache
sudo certbot --apache -d your_domain_or_IP

echo "Setup completed successfully! Your Flask application is now running on HTTPS."