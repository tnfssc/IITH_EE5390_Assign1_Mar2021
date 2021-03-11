#include <stdio.h>
#include <string.h>
#include <math.h>

void printFrequency(int freq[])
{
  long double entropy = 0;
  for (int i = 0; i < 26; i++)
  {
    if (freq[i] != 0)
    {
      entropy += (freq[i] / 1000 * (log10(freq[i] / 1000) / log10(2)));
      printf("%c - %d\n",
             i + 'a', freq[i]);
    }
  }
  printf("entropy %lf", entropy);
}
void findFrequncy(char S[])
{
  int i = 0;
  int freq[26] = {0};
  while (S[i] != '\0')
  {
    freq[S[i] - 'a']++;

    i++;
  }
  printFrequency(freq);
}

int main()
{
  char S[1000];
  FILE *fptr;
  if ((fptr = fopen("inputfile_problem2_58.txt", "r")) == NULL)
  {
    printf("Error! opening file");
    return 0;
  }
  fscanf(fptr, "%[^\n]", S);
  findFrequncy(S);
  fclose(fptr);
}