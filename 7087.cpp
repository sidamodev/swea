#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
  int test_case;
  int T;
  cin >> T;

  for (test_case = 1; test_case <= T; test_case++)
  {

    int N;
    int cnt = 0;
    cin >> N;
    string str[N];
    int cntArr[26];
    for (int i = 0; i < 26; i++)
    {
      cntArr[i] = -1;
    }
    for (int i = 0; i < N; i++)
    {
      cin >> str[i];
    }
    for (int i = 0; i < N; i++)
    {
      if (cntArr[str[i][0] - 65] == -1)
      {
        cntArr[str[i][0] - 65] = i;
      }
    }
    if (cntArr[0] > -1)
    {
      for (int i = 0; i < 26; i++)
      {
        if (cntArr[i] > -1)
          cnt++;
        else
          break;
      }
    }
    cout << '#' << test_case << ' ' << cnt << endl;
  }
  return 0;
}
