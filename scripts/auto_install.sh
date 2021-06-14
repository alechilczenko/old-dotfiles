#!/bin/bash
#Automatizing some stuff
#Make sure you have installed yay
#Don't launch with SUDO

function install {
    A='sudo pacman'

    pacman_packages=(i3lock i3-gaps blueman thunar alacritty vlc firefox scrot rofi zsh qpdfview geeqie nano flameshot neofetch feh lxappearance asciiquarium cmatrix gpick virtualbox filezilla pavucontrol brightnessctl nitrogen geany arandr xrandr gparted pamixer papirus-icon-theme)

    yay_packages=(polybar autotiling picom-ibhagwan-git nerd-fonts-complete pipes.sh rofi-bluetooth-git rofi-wifi-menu-git)

    $A -Syu && $A -S ${pacman_packages[@]}
    yay -S ${yay_packages[@]}
    
}
function moving_files {
    for I in $( ls $HOME/dotfiles/config ); do
        echo 'MOVING FOLDERS'
        echo $I
        cp -r $HOME/dotfiles/config/$I $HOME/.config
    done
}
function files {
    if [ -d "$HOME/.config" ]; then
        moving_files
    else
        echo 'CREATING .CONFIG FOLDER'
        mkdir $HOME/.config
        moving_files
    fi
}
function repos {
    git clone https://github.com/PapirusDevelopmentTeam/papirus-folders.git
    cd papirus-folders
    ./papirus-folders -t ePapirus -C violet
}

install
files
repos

