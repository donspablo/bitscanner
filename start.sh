#! /bin/bash -

BLA_filling_bar=( 0.25 '█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '██████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '██████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '███████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒' '███████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒' '████████████████████▒▒▒▒▒▒▒▒▒▒▒▒' '█████████████████████▒▒▒▒▒▒▒▒▒▒▒' '██████████████████████▒▒▒▒▒▒▒▒▒▒' '███████████████████████▒▒▒▒▒▒▒▒▒' '████████████████████████▒▒▒▒▒▒▒▒' '█████████████████████████▒▒▒▒▒▒▒' '██████████████████████████▒▒▒▒▒▒' '███████████████████████████▒▒▒▒▒' '████████████████████████████▒▒▒▒' '█████████████████████████████▒▒▒' '██████████████████████████████▒▒' '███████████████████████████████▒' '████████████████████████████████')

BLA_modern_metro=( 0.15 ▰▱▱▱▱▱▱ ▰▰▱▱▱▱▱ ▰▰▰▱▱▱▱ ▱▰▰▰▱▱▱ ▱▱▰▰▰▱▱ ▱▱▱▰▰▰▱ ▱▱▱▱▰▰▰ ▱▱▱▱▱▰▰ ▱▱▱▱▱▱▰ ▱▱▱▱▱▱▱ ▱▱▱▱▱▱▱ ▱▱▱▱▱▱▱ ▱▱▱▱▱▱▱ )
BLA_pong=( 0.35 '▐⠂       ▌' '▐⠈       ▌' '▐ ⠂      ▌' '▐ ⠠      ▌' '▐  ⡀     ▌' '▐  ⠠     ▌' '▐   ⠂    ▌' '▐   ⠈    ▌' '▐    ⠂   ▌' '▐    ⠠   ▌' '▐     ⡀  ▌' '▐     ⠠  ▌' '▐      ⠂ ▌' '▐      ⠈ ▌' '▐       ⠂▌' '▐       ⠠▌' '▐       ⡀▌' '▐      ⠠ ▌' '▐      ⠂ ▌' '▐     ⠈  ▌' '▐     ⠂  ▌' '▐    ⠠   ▌' '▐    ⡀   ▌' '▐   ⠠    ▌' '▐   ⠂    ▌' '▐  ⠈     ▌' '▐  ⠂     ▌' '▐ ⠠      ▌' '▐ ⡀      ▌' '▐⠠       ▌' )

declare -a BLA_active_loading_animation

BLA::play_loading_animation_loop() {
  while true ; do
    for frame in "${BLA_active_loading_animation[@]}" ; do
      printf "\r%s" "${frame}"
      sleep "${BLA_loading_animation_frame_interval}"
    done
  done
}

BLA::start_loading_animation() {
  BLA_active_loading_animation=( "${@}" )
  # Extract the delay between each frame from array BLA_active_loading_animation
  BLA_loading_animation_frame_interval="${BLA_active_loading_animation[0]}"
  unset "BLA_active_loading_animation[0]"
  tput civis # Hide the terminal cursor
  BLA::play_loading_animation_loop &
  BLA_loading_animation_pid="${!}"
}

BLA::stop_loading_animation() {
  kill "${BLA_loading_animation_pid}" &> /dev/null
  printf "\n"
  tput cnorm # Restore the terminal cursor
}



# Check if another instance of script is running
if pidof -o %PPID -x -- "$0" >/dev/null; then
  printf >&2 '%s\n' "ERROR: Script $0 already running"
  exit 1
fi
cd "$(dirname "$0")"
#sh ./stop.sh
clear
echo ""
echo " 🏁 Checking requirements..."
echo ""
BLA::start_loading_animation "${BLA_filling_bar[@]}"
pip install -r requirements.txt &> /dev/null
BLA::stop_loading_animation
clear
cd ./app
echo ""
echo " 🚀 Memcache initializing..."
echo ""
BLA::start_loading_animation "${BLA_filling_bar[@]}"
./memcached -n 70 -m 5200 -M -t 12 || memcached -n 70 -m 5200 -M -t 12 & sleep 5 &> /dev/null
BLA::stop_loading_animation
clear
echo ""
echo " Bitscanner engines initializing, please standby (keep this terminal open)  "
echo ""
echo " ██████╗░██╗████████╗░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░"
echo " ██╔══██╗██║╚══██╔══╝██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗"
echo " ██████╦╝██║░░░██║░░░╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝"
echo " ██╔══██╗██║░░░██║░░░░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗"
echo " ██████╦╝██║░░░██║░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║"
echo " ╚═════╝░╚═╝░░░╚═╝░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝"
echo ""
echo " note: locate your memcache process when memory reaches 4.1GB scan begins"
echo " windows: press + hold the win, shift + esc to load Task Manager"
echo " linux: run 'top' in the terminal to see your system processes"
echo ""
BLA::start_loading_animation "${BLA_pong[@]}" "Scaning"
python ./bitscanner.py || python2 ./bitscanner.py || python3 ./bitscanner.py &> /dev/null
BLA::stop_loading_animation
