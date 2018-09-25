#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <cstring>
using namespace std;

int main() {
  system("python data.py");
  double ptsAv = 0, trbAv = 0, astAv = 0, stlAv = 0, blkAv = 0, fgpAv = 0, fgaAv = 0, ftpAv = 0, ftaAv = 0, tovAv = 0, tpmAv = 0;
  double ptsIn = 0, trbIn = 0, astIn = 0, stlIn = 0, blkIn = 0, fgpIn = 0, fgaIn = 0, ftpIn = 0, ftaIn = 0, tovIn = 0, tpmIn = 0;
  string input = "";
  ifstream in;
  in.open("data.txt");
  
  if (!in) {
    cout << "Cannot open current data file.\n";
    return -1;
  }
  getline(in, input);
  ptsAv = atof(input.c_str());
  getline(in, input);
  trbAv = atof(input.c_str());
  getline(in, input);
  astAv = atof(input.c_str());
  getline(in, input);
  stlAv = atof(input.c_str());
  getline(in, input);
  blkAv = atof(input.c_str());
  getline(in, input);
  fgpAv = atof(input.c_str());
  getline(in, input);
  ftpAv = atof(input.c_str());
  getline(in, input);
  tovAv = atof(input.c_str());
  getline(in, input);
  tpmAv = atof(input.c_str());
  getline(in, input);
  fgaAv = atof(input.c_str());
  getline(in, input);
  ftaAv = atof(input.c_str());
  in.close();

  cout << "Points: ";
  cin >> ptsIn;
  cout << "Rebounds: ";
  cin >> trbIn;
  cout << "Assists: ";
  cin >> astIn;
  cout << "Steals: ";
  cin >> stlIn;
  cout << "Blocks: ";
  cin >> blkIn;
  cout << "Field Goal Percentage (In Decimal): ";
  cin >> fgpIn;
  cout << "Field Goal Attempts: ";
  cin >> fgaIn;
  cout << "Free Throw Percentage (In Decimal): ";
  cin >> ftpIn;
  cout << "Free Throw Attempts: ";
  cin >> ftaIn;
  cout << "Turnovers: ";
  cin >> tovIn;
  cout << "Three Pointers Made: ";
  cin >> tpmIn;
  
  // Declaration and points computation
  double stat = ptsIn;
  // Rebounds computation
  double inter = ptsAv / trbAv;
  inter *= trbIn;
  stat += inter;
  // Assists computation
  inter = ptsAv / astAv;
  inter *= astIn;
  stat += inter;
  // Steals computation
  inter = ptsAv / stlAv;
  inter *= stlIn;
  stat += inter;
  // Blocks computation
  inter = ptsAv / blkAv;
  inter *= blkIn;
  stat += inter;
  // Threes computation
  inter = ptsAv / tpmAv;
  inter *= tpmIn;
  stat += inter;
  // Field Goal Percentage Compuation
  inter = fgpIn - fgpAv;
  inter = inter / fgpAv;
  inter *= fgaIn;
  inter *= ptsAv;
  inter = inter / fgaAv;
  stat += inter;
  // Free Throw Percentage Computation
  inter = ftpIn - ftpAv;
  inter = inter / ftpAv;
  inter *= ftaIn;
  inter *= ptsAv;
  inter = inter / ftaAv;
  stat += inter;
  // Turnover Computation
  inter = ptsAv / tovAv;
  inter *= tovIn;
  stat -= inter;
  printf("The computed statistic is %f\n", stat);
  return 0;
}
