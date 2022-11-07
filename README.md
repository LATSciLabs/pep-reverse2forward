Supplements scripts provided in Rebollo et al. (2014) (https://doi.org/10.1093/nar/gku940) for Illumina sequencing of 
phage display libraries. This is because Illumina is provided as both forward and reverse reads of sequences, the latter of which
previously would be seemingly disregarded despite slight differences in read counts between them.

Initially Created on Mon Apr 11 16:01:02 2022

Last Updated: 07/11/2022

"Reverse Read TL"
>Take reverse read from phage library sequencing (after Step2 of Rebollo scripts)
1. Translate the provided DNA sequence into the forward equivalent
2. Translate this into the respective peptide sequence
3. Have this in place instead!
>>Note: In phage libraries, the easy tell in "is this forward or not"
>>is the cysteines being detected in the correct spots (in cyclics). 
>>If your sequence does not have this, use the left/forward primer
>>sequence as your guide.
