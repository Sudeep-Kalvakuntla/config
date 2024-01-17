/*
In the SCRABBLE Crossword Game, players form words using small tiles, each
containing a letter and a face value. The face value varies from one letter to
another, based on the letter’s rarity.
( Here are the face values: I : AEILNORSTU. 2: DC., 3: BCMP. 4: FHVWY. 5: K. X:
JX. 10: QZ. ) Write a program that computes the value of a word by summing the
values of its letters:
*/
#include <ctype.h>
#include <stdio.h>

int main(void) {
  char i = 'a';
  int score = 0;
  printf("Enter a word: ");
  scanf("");

  do {
    i = getchar();

    if (toupper(i) == 'A' || toupper(i) == 'E' || toupper(i) == 'I' ||
        toupper(i) == 'L' || toupper(i) == 'N' || toupper(i) == 'O' ||
        toupper(i) == 'R' || toupper(i) == 'S' || toupper(i) == 'T' ||
        toupper(i) == 'U') {
      score += 1;
    } else if (toupper(i) == 'D' || toupper(i) == 'G') {
      score += 2;
    } else if (toupper(i) == 'B' || toupper(i) == 'C' || toupper(i) == 'M' ||
               toupper(i) == 'P') {
      score += 3;
    } else if (toupper(i) == 'F' || toupper(i) == 'H' || toupper(i) == 'V' ||
               toupper(i) == 'W' || toupper(i) == 'Y') {
      score += 4;
    } else if (toupper(i) == 'K') {
      score += 5;
    } else if (toupper(i) == 'J' || toupper(i) == 'X') {
      score += 8;
    } else if (toupper(i) == 'Q' || toupper(i) == 'Z') {
      score += 10;
    }
  } while (i != '\n');

  printf("Scrabble value: %d", score);
  return 0;
}
