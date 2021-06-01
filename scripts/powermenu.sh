#!/bin/bash

# options to be displayed
option0="Lock"
option1="Log out"
option2="Suspend"
option3="Reboot"
option4="Shutdown"

# options passed into variable
options="$option0\n$option1\n$option2\n$option3\n$option4"

chosen="$(echo -e "$options" | rofi -lines 5 -dmenu -p "power")"
case $chosen in
    $option0)
        $HOME/.scripts/i3lock/lock;;
    $option1)
        i3-msg exit;;
    $option2)
        systemctl suspend;;
    $option3)
      	systemctl reboot;;
    $option4)
        systemctl poweroff;;
esac
