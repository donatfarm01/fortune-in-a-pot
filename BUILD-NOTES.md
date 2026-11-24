Build notes for the Fortune in a Pot entry.

The entry is a single fortune line for a houseplant, written to sound like a prediction rather than a slogan or a care instruction. It names the plant on the windowsill through its newest leaf and the room around it, so it reads as a fortune for this plant in this window, not for any plant anywhere. The joke is small and warm: the plant thrives so visibly that even the cat, the classic houseplant menace, leaves it alone. There is no doom, no withering, and no mockery in it, and it reads cleanly aloud in one breath.

The program is a short Python script at the repository root. It holds the fortune as one constant and writes it exactly, with no trailing newline, to the output entry file. The repository also carries a readme built from the competition template with the three make.fun badges linked to the bounty page, and a MIT license file carrying the SPDX identifier line.

Verification was done by running the program fresh and reading back the output file, then counting its characters and hashing it both with and without a trailing newline. The kit check was run locally from the unpacked kit directory against this repository, and its result is recorded in the final report.

One placeholder remains for the parent to fill in: the referral code in the readme footer link is left as the template wrote it, because the builder session holds no referral code. The check reports that placeholder but never refuses an entry for it.
