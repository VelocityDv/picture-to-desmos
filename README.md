# picture-to-desmos
turning a picture to desmos art using python

Install all requirements by calling pip install -r requirements.txt

Alongside, potrace and java is also required. For arch linux users to install potrace
```console
sudo pacman -S potrace
```
For windows and macos users. sort it out yourself. http://potrace.sourceforge.net/#downloading

Run `python preprocess_image.py threshold filename` which will create a output file for you to copy and paste into desmos.
The `threshhold` controls the amount of outline for the jpg. The 'threshold' number is from 0 - 255 where the higher the number the less detail in lines. 

basically stole a bunch of shit and made it work. 
in the future I am going to recreate all the shit I stole. 

