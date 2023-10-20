import os
# from audio_synthetizer import synthetize

def syllab_to_ipa_text(syllab):
    return syllab['c']['ipa'] + syllab['v']['ipa']

def syllab_to_hr_text(syllab, strees=False):
    if strees:
        return syllab['c']['hr'] + syllab['v']['hrs']
    else:
        return syllab['c']['hr'] + syllab['v']['hr']

def syllabs_to_ipa_text(syllab1, syllab2):
    return syllab_to_ipa_text(syllab1) + '.ˈ' + syllab_to_ipa_text(syllab2)

def syllabs_to_hr_text(syllab1, syllab2, strees=False):
    return syllab_to_hr_text(syllab1, strees) + syllab_to_hr_text(syllab2, strees)

def syllabs_are_different(syllab1, syllab2):
    return syllab1['c']['hr'] != syllab2['c']['hr'] or syllab1['v']['hr'] != syllab2['v']['hr']

def goldstein_matrix(unit):
    print('\t'+'\t'.join(unit))
    for s1 in unit:
        print(s1, end='\t')
        for s2 in unit:
            print(syllabs_to_ipa_text(s1, s2), end='\t')
        print()

def goldstein_matrix(syllabs, IPA=True):
    if IPA:
        print('\t'+'\t'.join([syllab_to_ipa_text(s) for s in syllabs]))
    else:
        print('\t'+'\t'.join([syllab_to_hr_text(s) for s in syllabs]))
    for s1 in syllabs:
        if IPA:
            print(syllab_to_ipa_text(s1), end='\t')
        else:
            print(syllab_to_hr_text(s1), end='\t')
        for s2 in syllabs:
            if IPA:
                print(syllabs_to_ipa_text(s1, s2), end='\t')
            else:
                print(syllabs_to_hr_text(s1, s2), end='\t')
        print()

def save_to_tab_delimited_file(syllabs, filename, IPA=True):
    with open(filename, 'w', encoding='utf-8') as f:
        if IPA:
            f.write('\t'+'\t'.join([syllab_to_ipa_text(s) for s in syllabs]) + '\n')
        else:
            f.write('\t'+'\t'.join([syllab_to_hr_text(s) for s in syllabs]) + '\n')
        for s1 in syllabs:
            if IPA:
                f.write(syllab_to_ipa_text(s1) + '\t')
            else:
                f.write(syllab_to_hr_text(s1) + '\t')
            for s2 in syllabs:
                if IPA:
                    f.write(syllabs_to_ipa_text(s1, s2) + '\t')
                else:
                    f.write(syllabs_to_hr_text(s1, s2) + '\t')
            f.write('\n')

# consonants
PlosiveBilabial = {'ipa':'b', 'hr':'b'}
NonSibilantFricative = {'ipa':'f', 'hr':'f'}
LateralApproximantAlveolar = {'ipa':'l', 'hr':'l'}
NasalAlveolar = {'ipa':'n', 'hr':'n'}

# vowels
OpenFront = {'ipa':'a', 'hr':'a', 'hrs':'á'}
OpenMidFront = {'ipa':'ɛ', 'hr':'e', 'hrs':'é'}
CloseFront = {'ipa':'i', 'hr':'i', 'hrs':'í'}
OpenMidBack = {'ipa':'ɔ', 'hr':'o', 'hrs':'ó'}

Consonants = [PlosiveBilabial, NonSibilantFricative, LateralApproximantAlveolar, NasalAlveolar]
Vowels = [OpenFront, OpenMidFront, CloseFront, OpenMidBack]
Syllabs = [{'c':c, 'v':v} for c in Consonants for v in Vowels]

# goldstein_matrix(Syllabs)
# save_to_tab_delimited_file(Syllabs, 'syllabs.txt')

Words = [{'ipa': syllabs_to_ipa_text(s1, s2), 'hrs':syllabs_to_hr_text(s1, s2, True), 'hr':syllabs_to_hr_text(s1, s2, False)} \
        for s1 in Syllabs for s2 in Syllabs]

for Word in Words:
    print(Word['hr'].lower())
# print(Vowels)
# print(Consonants)
# print(Syllabs)
# print(Words)
# folder_name = 'ipa'
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)
# for word in Words:
#     synthetize(word, 'ipa/' + item['hr'].upper() + '.wav')