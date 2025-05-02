<h1 align=center>My Dots <img src="https://cdn-icons-png.flaticon.com/512/2134/2134212.png" width=60 align=center></img></h1> 

<div align=center>
  <a href="https://github.com/janleigh/dotfiles/">
    <img src="https://img.shields.io/github/repo-size/felipevcc/dotfiles?color=6E93CC&labelColor=1a1e29&style=for-the-badge">
  </a> 
</div> <br>

<div align=center>
  
  [Previews](#previews) · [Info](#info) · [Note](#note) · [Credits](#credits)
</div> <br>

## Previews 
<img src="https://i.imgur.com/c5NGLTq.png"></img>
<img src="https://i.imgur.com/IVErtro.png"></img>
<img src="https://i.imgur.com/YjW7Zfn.png"></img>

## Info 
* **OS:** [Manjaro Linux](https://manjaro.org/) 
* **WM:** [Bspwm](https://github.com/baskerville/bspwm)
* **Bar:** [Polybar](https://github.com/polybar/polybar) 
* **Terminal:** [Alacritty](https://github.com/alacritty/alacritty)
* **Shell:** [Zsh](https://wiki.archlinux.org/title/zsh) 
* **Compositor:** [Picom](https://github.com/yshui/picom)
* **App Launcher:** [Rofi](https://github.com/davatorium/rofi) - [Customization](https://github.com/adi1090x/rofi) 
* **Notifications:** [Dunst](https://github.com/dunst-project/dunst)
* **Prompt:** [Starship](https://starship.rs/)
* **Document Viewer:** [Zathura](https://github.com/pwmt/zathura)
* **Audio Visualizer:** [Cava](https://github.com/karlstav/cava)

## Note
* The polybar font is [JetbrainsMono Nerd Font](https://www.nerdfonts.com/font-downloads) and material design icon font for the icons. You can check this configuration in this file: [config.ini](https://github.com/felipevcc/dotfiles/blob/main/config/polybar/config.ini).
* In my bspwm I used a python script so every time I start bspwm the wallpaper changes. Inside the script I call a folder where I keep all the wallpapers. If you want to use the script you should set your wallpapers folder path [here](https://github.com/felipevcc/dotfiles/blob/main/config/bspwm/scripts/wallpaper.py), if you want to disable the script you should comment line 51 of bspwmrc and uncomment line 48 to set a wallpaper path.

<br>

## Credits
* The polybar configuration is based on [siduck's dotfiles](https://github.com/siduck/dotfiles) and currently I am also making use of the [Nvchad](https://github.com/NvChad/NvChad) configuration. 
* The cava color palette was taken from [here](https://github.com/lokesh-krishna/dotfiles/tree/main/catppuccin).
* I also used [Prayags Spotify modules setup](https://github.com/PrayagS/polybar-spotify).
