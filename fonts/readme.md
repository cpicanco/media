# Font Creation methodology

A text font (`Picanco et al.ttf`) was created to facilitate the presentation of textual stimuli.
The font was manually crafted using FontForge (https://fontforge.org):

`Picanco_et_al.ttf`: font file in TTF format (not fully compliant).   
`Picanco_et_al.sfd`: Sound Forge design file.   

The creation of each character in the font followed some steps.
First, a base character (O), a circular shape with a "hole" was distorted:

![Base character distortion](https://github.com/cpicanco/media/blob/main/docs/sound-forge-char-creation-illustration.png)

Following the distortion, the characters were inspected, and if they bore any striking resemblance to known characters or shapes, the process was redone.
Subsequently, they were vertically elongated, centered, and the horizontal spacing was uniformly reduced, maintaining the same vertical distance for all characters.
Finally, minor adjustments were made to prevent overlaps between support points of character design lines.

# Instructions for installing the font on a computer and using it in text editors

To install the font on Windows, simply double-click the `Picanco et al.ttf` file and then click "Install." Afterward, the font will be listed in the font selection menu of programs such as Microsoft Word, Libre Office, etc., as `Picanco et al.`.

# Free Pascal SDL2 code examples for loading and using the font inside programs
If you are a developer, take a look on how you can load and render the font here with SDL2:
- [Managing many fonts](https://github.com/cpicanco/stimulus-control-sdl2/blob/main/src/sdl.app.text.pas)
- [Rendering a font](https://github.com/cpicanco/stimulus-control-sdl2/blob/main/src/sdl.app.graphics.text.pas)
