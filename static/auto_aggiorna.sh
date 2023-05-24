#!/bin/bash

color_normal="$(tput sgr0)"
color_bold="$(tput bold)"
color_green="$(tput setaf 77)"
color_orange="$(tput setaf 214)"

echo
echo "-------------------------------"
echo "${color_bold}${color_green}[#]${color_normal} ${color_bold}${color_orange}Calminaro Update System${color_normal} ${color_bold}${color_green}[#]${color_normal}"
echo "-------------------------------"
echo

echo "Aggiornamento automatico dei repository e dei pacchetti .deb e Flatpak."
echo "Gli aggiornamenti vengono eseguiti come amministratore, ti sarà richiesto di inserire la password utente."
echo
sudo apt -qq update
sudo apt -qq full-upgrade -y
sudo apt -qq autoremove -y
sudo apt -qq clean
sudo flatpak --noninteractive update -y

echo
echo "Aggiornamento terminato!"
if [[ $1 == "easter" ]] ; then
  sudo apt -qq install sl -y
  sl
fi
