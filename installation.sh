#!/bin/bash

# Icon:
echo "··································································";
echo ":                                                                :";
echo ":                                                                :";
echo ":                                                                :";
echo ":                                                                :";
echo ":                                                                :";
echo ":     ███╗   ███╗███████╗ ██████╗██████╗ ██╗██████╗ ███████╗     :";
echo ":     ████╗ ████║██╔════╝██╔════╝██╔══██╗██║██╔══██╗██╔════╝     :";
echo ":     ██╔████╔██║███████╗██║     ██████╔╝██║██████╔╝█████╗       :";
echo ":     ██║╚██╔╝██║╚════██║██║     ██╔══██╗██║██╔══██╗██╔══╝       :";
echo ":     ██║ ╚═╝ ██║███████║╚██████╗██║  ██║██║██████╔╝███████╗     :";
echo ":     ╚═╝     ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝     :";
echo ":                                                                :";
echo ":                                                                :";
echo ":                                                                :";
echo ":                                                                :";
echo ":                                                                :";
echo "··································································";

# General Information
VERSION=$(grep -Eroh 'v[0-9]+\.[0-9]+\.[0-9]+' src/ 2>/dev/null)
echo "mscribe $VERSION Installation"
sleep 2

# Linux Credentials
echo "Linux Credentials"
read -p "Enter Linux username [default: mscribe]: " linux_username
linux_username=${linux_username:-mscribe}
linux_username=$(echo "$linux_username" | xargs)

sudo adduser "$linux_username"
sudo groupadd app
sudo usermod -aG app $linux_username

mkdir -p /app

# Database Credentials
echo "MySQL Database Credentials"
read -p "Enter database host [default: localhost]: " database_host
database_host=${database_host:-localhost}

read -p "Enter database user [default: mscribe]: " database_user
database_user=${database_user:-mscribe}

echo -n "Enter database password: "
stty -echo
read database_password
stty echo
echo

read -p "Enter database schema [default: mscribe]: " database_schema
database_schema=${database_schema:-mscribe}

read -p "Enter database port [default: 3306]: " database_port
database_port=${database_port:-3306}

# Variables
IP=$(hostname -I | awk '{print $1}')
APP_PATH="/app"

# Installation
echo "Updating and upgrading the system..."
sudo apt update && sudo apt upgrade -y

echo "Installing prerequisites..."
sudo apt install -y software-properties-common mysql-client

echo "Adding Deadsnakes PPA for Python 3.10..."
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

echo "Installing Python 3.10 and required packages..."
sudo apt install -y python3.10 python3.10-venv python3.10-dev libmysqlclient-dev nginx

echo "Installing pip for Python 3.10..."
python3.10 -m ensurepip
python3.10 -m pip install --upgrade pip

# Create virtual environment
echo "Creating a virtual environment..."
python3.10 -m venv $APP_PATH/environment/

# Activate the virtual environment
source $APP_PATH/environment/bin/activate

# Install project dependencies
echo "Installing project dependencies..."
pip3 install -r requirements.txt
pip3 install gunicorn

# Permissions
echo "Setting permissions for project files..."
sudo mkdir -p $APP_PATH/mscribe
sudo mv * $APP_PATH/mscribe/

# Database Setup
if [[ "$database_host" == "localhost" ]]; then
    echo "Installing and configuring MySQL server..."
    sudo apt install -y mysql-server
    sudo mysql_secure_installation
fi

echo "Configuring MySQL database and user..."
sudo mysql -e "CREATE DATABASE IF NOT EXISTS \`$database_schema\`;"
sudo mysql -e "CREATE USER IF NOT EXISTS '$database_user'@'$database_host' IDENTIFIED BY '$database_password';"
sudo mysql -e "GRANT ALL PRIVILEGES ON \`$database_schema\`.* TO '$database_user'@'$database_host';"
sudo mysql -e "FLUSH PRIVILEGES;"

# Gunicorn Setup
echo "Setting up Gunicorn service..."
sudo bash -c "cat <<EOL > /etc/systemd/system/mscribe.service
[Unit]
Description=Gunicorn instance to serve mscribe application
After=network.target

[Service]
User=$linux_username
Group=app
WorkingDirectory=/app/mscribe/src
Environment="PATH=/app/environment/bin"
Environment="DATABASE_HOST=$database_host"
Environment="DATABASE_USERNAME=$database_user"
Environment="DATABASE_PASSWORD=$database_password"
Environment="DATABASE_SCHEMA=$database_schema"
Environment="DATABASE_PORT=$database_port"
ExecStart=/app/environment/bin/gunicorn --workers 3 --bind unix:/app/mscribe/mscribe.sock app:app

Restart=on-failure
RestartSec=15

[Install]
WantedBy=multi-user.target
EOL"

chown -R $linux_username:app /app
chmod -R 775 /app

# Nginx Configuration
echo "Configuring Nginx..."
sudo tee /etc/nginx/sites-available/mscribe > /dev/null <<EOL
server {
    listen 80;
    server_name $IP;

    location / {
        proxy_pass http://unix:$APP_PATH/mscribe/mscribe.sock;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    }

    error_log /var/log/nginx/mscribe_error.log;
    access_log /var/log/nginx/mscribe_access.log;
}
EOL

sudo ln -s /etc/nginx/sites-available/mscribe /etc/nginx/sites-enabled
rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl enable nginx

sudo systemctl daemon-reload
sudo systemctl start mscribe
sudo systemctl enable mscribe

# Completion
echo "Setup completed successfully! Your Flask app is available at http://$IP/"
