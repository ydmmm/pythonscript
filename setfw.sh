#!/bin/bash
function rules
{
    iptables -I INPUT -p tcp --dport 80 -j ACCEPT
}
if systemctl status iptables>>/dev/null 
then 
    rules
    echo "iptables rules setted!"
else
    systemctl start iptables
    echo "iptables started!"
    rules
    echo "iptables rules setted!"
fi
systemctl status iptables
