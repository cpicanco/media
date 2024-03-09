# Picanco et al media files
Here lives an LFS (https://git-lfs.com/) repository for media files used to stimuli presentation in experimental research using [Stimulus Control SDL2](https://github.com/cpicanco/stimulus-control-sdl2/) software. Research topics includes teaching and assessment of reading skills (with and without comprehension) using an artificially constructed linguistic system (also known as constructed language or COLANG).

This repository contains all `*.png`, `*.ttf`, `*.wav` media files of the COLANG.

## An artificially constructed linguistic system

The COLANG consists of 4 consonants, 4 vowels, and `cvcv` pseudowords (`c` and `v` meaning consonant and vowel, respectively) with primary emphasis at the second syllable (see [Hanna et al. (2011)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3014779/)). This system allows, through combination, the creation of syllables (N = 16) and words (N = 256).

## Equivalence Classes and conventions
An equivalence class, in Behavior Analysis, refers to stimuli that can be behaviorally interchanged by one another in a context with physical support to do so. [The software](https://github.com/cpicanco/stimulus-control-sdl2/) uses some complementary conventions to ease the communication when refering to sensorial modalities, and either specific classes or specific class members.

### Convention of class sensorial modality
For trials that implements the "Relation" parameter, one must use the following capital letters to specify the desired sensorial modality of a class: 

`A` means auditive stimuli presented to the participant;   
`B` means pictures as visual stimuli presented to the participant;   
`C` means text as visual stimuli presented to the participant, and;   
`D` means participant's speech (words spoken by participants and recorded by the software).

### Convention of classes used as sample or comparison
For trials that implements the "Relation" parameter, one must write relations as `{S}-{C}` where `{S}` and `{C}` are placeholders for `sample modality` and `comparison modality`. So, assuming the following matching-to-sample framework:
- fixed single sample (multiple samples are possible with major adjustments);
- up to three comparisons (more are possible with adjustments);
- participant driven response requirements for sample and comparison (limited hold is also possible with adjustments);
- 0-delayed comparisons after a response to the sample (without delay also possible with minor adjustments);
- simultaneous presentation of visual comparisons (and visual component of auditive comparisons too);
- participant driven successive presentation of auditive stimuli (sample and comparisons);
- participant driven recording of speech;
  
the following relations were implemented:

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

and the following relations were not implemented, they are kept here for reference only:

`A-D` means auditive-vocal, sound-to-speech arbitrary task   
`D-D` means vocal-vocal, speech-to-speech task (self echoic behavior?)   
`D-A` means vocal-auditive, speech-to-sound task   
`D-B` means vocal-visual, speech-to-picture   
`D-C` means vocal-visual, speech-to-text.

Hence, after teaching `A-B` and `A-C` MTS tasks, a participant may demonstrates reading comprehension during `C-B` and `C-D` assessments.

### Convention for media files and class members correspondence: pseudowords
The [the software](https://github.com/cpicanco/stimulus-control-sdl2/) assumes that each `cvcv` pseudoword is an Stimulus Equivalence Class. The root folder of this repository is the default `media` folder of [the software](https://github.com/cpicanco/stimulus-control-sdl2/):

- Inside the `wav` folder, `cvcv.wav` files are loaded as `A` stimuli.   
- Inside the `png` folder, `cvcv.png` files are loaded as `B` stimuli.   
- Inside the `font` fonder, `cvcv` text are rendered from a `.ttf` font file loaded as `C` stimuli or `D` stimuli. For `D` stimuli, words spoken by participants are recorded during the experiment. They are save outside the `media` folder with unique identifiers to avoid overriding in case of multiple responses in the same trial.

### Convention for media files and class members correspondence: drag-n-drop
Multiple samples and multiple comparisons may be presented simultaneously on the screen using `drag-n-drop` trials. For them, the above mentioned conventions do not apply (it is a work-in-progress). Currently, only figure-to-figure relations were implemented, the software will load only `B` stimuli from files.

One can create a folder inside the `png` folder and the software will search for files inside it. One must name each file using the following convention: two character alphanumeric codes where letters are class members and numbers are class names. For example, the `png\alpha_numeric_convention\` folder contains `A1.png`, `A2.png`, `A3.png`, `B1.png`, `B2.png`, `B3.png`, and `C1.png`, `C2.png`, `C3.png` files. Then, the software will known you have Class 1 with A1, B1, C1 as members, Class 2 with A2, B2, C2 as members, and Class 3 with A3, B3, C3 as members.
