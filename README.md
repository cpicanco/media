# Picanco et al media files
Here lives an LFS (https://git-lfs.com/) repository for media files used to stimuli presentation in experimental research using [Stimulus Control SDL2](https://github.com/cpicanco/stimulus-control-sdl2/) software. Research topics includes teaching and assessment of reading skills (with and without comprehension) using an artificially constructed linguistic system (also known as constructed language or COLANG).

This repository contains all `*.png`, `*.ttf`, `*.wav` media files of the COLANG.

## An artificially constructed linguistic system

The COLANG consists of 4 consonants, 4 vowels, and `cvcv` pseudowords (`c` and `v` meaning consonant and vowel, respectively) with primary emphasis at the second syllable (see [Hanna et al. (2011)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3014779/)). This system allows, through combination, the creation of syllables (N = 16) and words (N = 256).

## A word as an Equivalence Class
Throughout an experimental session, [the software](https://github.com/cpicanco/stimulus-control-sdl2/) assumes that each `cvcv` pseudoword is an Stimulus Equivalence Class ([Sidman, 2000](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1284788/)). Equivalence Classes are used, for example, for teaching and assessment of reading comprehension. In Behavior Analysis, the terminology of Equivalence Classes usually reserves capital words for each class. Here, we assume that:

`A` means auditive stimuli presented to the participant;   
`B` means pictures as visual stimuli presented to the participant;   
`C` means text as visual stimuli presented to the participant, and;   
`D` means participant's speech (for example, words spoken by participants).

Many relations can be built from those classes and used to design teaching and assessment tasks. Assuming the following matching-to-sample framework:
- relations defined as `{S}-{C}` where `{S}` and `{C}` are placeholders for `sample class` and `comparison class`
- fixed single sample (multiple samples are possible with major adjustments);
- up to three comparisons (more are possible with adjustments);
- participant driven response requirements for sample and comparison (limited hold is also possible with adjustments);
- 0-delayed comparisons after a response to the sample (without delay also possible with minor adjustments);
- simultaneous presentation of visual comparisons (and visual component of auditive comparisons too);
- participant driven successive presentation of auditive stimuli (sample and comparisons);
- participant driven recording of speech;

the following relations are meaningful:

`A-A` means auditive-auditive, sound-to-sound task (sound identity);   
`B-B` means visual-visual, picture-to-picture task (picture identity);   
`C-C` means visual-visual, text-to-text identity task (text identity);   
`A-B` means auditive-visual, sound-to-picture task (arbitrarity, word listening, word comprehension);   
`A-C` means auditive-visual, sound-to-text arbitrary task (arbitrarity, word listening, word reading);   
`B-A` means visual-auditive, picture-to-sound task (arbitrarity, word listening);   
`B-C` means visual-visual, picture-to-text task (arbitrarity, word reading comprehension);   
`B-D` means visual-vocal, picture-to-speech task (naming pictures, tact);   
`C-A` means visual-auditive, text-to-sound task (word reading, word listening);   
`C-B` means visual-auditive, text-to-picture task (word reading);   
`C-D` means visual vocal text-to-speech task (naming words, tact).

Some relations (although possible to be executed strictly following the previous matching-to-sample framework) are not meaningful from the perspective of teaching and assessment of reading tasks and are kept here for reference only:

`A-D` means auditive-vocal, sound-to-speech arbitrary task   
`D-D` means vocal-vocal, speech-to-speech task (self echoic behavior?)   
`D-A` means vocal-auditive, speech-to-sound task   
`D-B` means vocal-visual, speech-to-picture   
`D-C` means vocal-visual, speech-to-text.


Hence, after teaching `A-B` and `A-C` MTS tasks, a participant may demonstrates reading comprehension during `C-B` and `C-D` assessments.

## Repository structure

The root folder of this repository is the default `media` folder of [the software](https://github.com/cpicanco/stimulus-control-sdl2/). The root folder is used to files effectively used for building equivalence classes, where:

`cvcv.wav` files are `A` stimuli.   
`cvcv.png` files are `B` stimuli.   
`cvcv` text (rendered from a `.ttf` font) are `C` stimuli and,   
`cvcv-spoken-{ID}.wav` files are `D` responses (words spoken by participants that were recorded and saved during the experiment, where {N} is a placeholder for an unique identifier in case of multiple responses).

Also, the root folder contains media files for special use cases during teaching and assessment:

`XXXX.png` files are `B` stimuli reserved for presenting negative comparisons that are never presented as positive comparisons.

The `assets`, `base`, and `docs` folder

### Assets folder

Media inside the `assets` folder are reserved for loading media once, and render throughout an experimental session (for `A` class of matching-to-sample tasks, images of buttons, and sound of consequences, for example).

### Docs folder

Media inside the `docs` folder are only for the current repository documentation and are not used in experiments.

### PNG files

PNG files are photos of unusual objects with transparent background. Their filenames indicates their confection method as follows:

`2XXX` filenames indicates files that were (1) copied from the "Novel Object and Unusual Name Database (NOUN): NOUN-2-600DPI Set" (https://stimuli.mit.edu/stimulus/555) dataset, and (2) have its background removed using an online AI background remover tool (https://zyro.com/) and manually using GIMP (when using the AI tool failed). The NOUN-2 dataset have Familiarity and Name-Ability scores and is maintained by Michael Hout (New Mexico State University), Jessica Horst (University of Sussex). The `base` folder contains the 24 most novel stimuli available in the 600dpi dataset.

`3XXX` filenames indicates files that were generated by AI (https://my.visme.co/) using input text containing words such as "strange asymmetrical object red green blue distorted".

`cvcv` filenames indicates `.png` files randomly copied from the `base` folder in such a way that they are correlated with (1) `cvcv` wav files and (2) `c` and `v` character of font files and used to render `cvcv` text of pseudowords used throughout an experimental session.

### WAV files

`cvcv` filenames are text-to-speech words synthesized using Microsoft's Speech Object Library (SAPI), with the following SSML template (for the word befo):

```xml
  Result := '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="pt-BR">' +
    '<voice name="Microsoft Maria Desktop - Portuguese(Brazil)">' +
      '<prosody rate="10%">' +
        '<phoneme alphabet="ipa" ph="bɛ.ˈfɔ">befo</phoneme>.'+
      '</prosody>'+
    '</voice>'+
  '</speak>';
```

During teaching, some sounds are used as differential consequences: 

`acerto` is a high pitch sound used as consequence for right responses.

`erro` is a low pitch sound used as consequence for wrong responses.


### TTF files

`Picanco_et_al.ttf`: font file in TTF format (not fully compliant).
`Picanco_et_al.sfd`: Sound Forge design file.


#### Font Creation methodology

A text font (`Picanco et al.ttf`) was created to facilitate the presentation of textual stimuli. The font was manually crafted using FontForge (https://fontforge.org). The creation of each character in the font followed some steps. First, a base character (O), a circular shape with a "hole" was distorted:

![Base character distortion](docs/sound-forge-char-creation-illustration.png)

Following the distortion, the characters were inspected, and if they bore any striking resemblance to known characters or shapes, the process was redone. Subsequently, they were vertically elongated, centered, and the horizontal spacing was uniformly reduced, maintaining the same vertical distance for all characters. Finally, minor adjustments were made to prevent overlaps between support points of character design lines.

#### Instructions for installing the font on a computer and using it in text editors

To install the font on Windows, simply double-click the `Picanco et al.ttf` file and then click "Install." Afterward, the font will be listed in the font selection menu of programs such as Microsoft Word, Libre Office, etc., as `Picanco et al.`.

#### Free Pascal SDL2 code examples for loading and using the font inside programs

- [Managing many fonts](https://github.com/cpicanco/stimulus-control-sdl2/blob/main/src/sdl.app.text.pas)
- [Rendering a font](https://github.com/cpicanco/stimulus-control-sdl2/blob/main/src/sdl.app.graphics.text.pas)