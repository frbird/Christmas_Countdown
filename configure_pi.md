# Introduction
I was able to run this successfully on a Raspberry Pi Zero 2 W.  The primary limitation on this platform is the memory.  It really can't run Chromium or Firefox very well since it only has 500Mb of RAM.  If you do use this platform you'll need to follow these directions exactly.  Other models of the Raspberry Pi will probably be quite a bit easier to configure.

## OS Installation 
This is pretty straightforward.  Flash an SD card with the Raspbian OS lite image.  This does not have a desktop environment but can run Chromium in kiosk mode.


## Configure the environment

>**Optional**
>
> If You intend to render the website from a local file you'll need to copy the `fonts` and `images` directories and the `countdown_website.html` file.  Make sure these are all in the same parent directory.

1. Install the required packages
    ```
    sudo apt update && sudo apt upgrade -y
    ```
    ```
    sudo apt install --no-install-recommends \
    xserver-xorg \
    x11-xserver-utils \
    xinit \
    openbox \
    chromium \
    unclutter -y
    ```

2. Configure the bash profile.

    Create the file `~/.bash_profile` if it doesn't already exist.  Add the following line at the end of the file.
    ```
    [[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && startx -- -nocursor
    ```

3. Create the autostart file to automatically launch the countdown webpage

    Create the file `~/.config/openbox/autostart` and add the following content to the file
    ```
    # Disable screensaver/power management
    xset s off
    xset s noblank
    xset -dpms

    # Hide mouse cursor
    unclutter &

    # Launch Chromium in kiosk mode after a short delay
    sleep 4
    chromium --kiosk \
    --disable-gpu \
    --no-memcheck \
    --disable-software-rasterizer \
    --start-maximized \
    --disable-component-update \
    --disable-infobars \
    --disable-session-crashed-bubble \
    --noerrdialogs \
    --no-sandbox \
    file:///home/user/index.html
    ```
    The last line is the URL for the webpage.  I've just had the Chromium render the file directly.  If you want to host the countdown webpage on an actual web server the use the appropriate URL rather than `file:///home/user/index.html`

4. That's it!  Reboot and the device and you should see the Countdown Clock come up in Kiosk mode!