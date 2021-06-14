if [ -d "$HOME/.local/share/PIBIC" ]; then
    rm -r $HOME/.local/share/PIBIC
    rm $HOME/.local/share/applications/PIBIC.desktop
fi

mkdir $HOME/.local/share/PIBIC
cp -r * $HOME/.local/share/PIBIC
cp PIBIC.desktop $HOME/.local/share/applications

echo Path=$HOME/.local/share/PIBIC >> $HOME/.local/share/applications/PIBIC.desktop
