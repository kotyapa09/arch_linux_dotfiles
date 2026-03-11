
# Create aliases
alias la='ls -la'

alias fetch='/home/user/bin/fetchs/fetch'
alias sysfetch='/home/user/bin/fetchs/sysfetch'

alias weather='/home/user/bin/weather'
alias prognose='/home/user/bin/weather2'

set -U fish_greeting
set fish_color_command green
set -gx EDITOR vim
set -gx VISUAL vim
set -gx BROWSER /usr/bin/firefox


if status is-interactive
    # Commands to run in interactive sessions can go here
end

sh /home/user/.config/fish/script.sh

zoxide init fish | source
