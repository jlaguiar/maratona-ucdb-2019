#include <bits/stdc++.h>

using namespace std;

int64_t gcd(int64_t a, int64_t b) {
  while (b) {
    a %= b;
    swap(a, b);
  }
  return a;
}

int64_t lcm(int64_t a, int64_t b) {
  return (a / gcd(a, b)) * b;
}

int main(int argc, char* argv[]) {

  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N, L;
  cin >> N >> L;

  int64_t t = 1;
  for (int i = 0; i < N; ++i) {
    int64_t x; cin >> x;
    t = lcm(t, x);
  }

  int best = 1;
  int best_lcm = t;

  for (int v = 2; v <= L; ++v) {
    auto lcm_v = lcm(t, v);
    if (lcm_v <= L && lcm_v > best_lcm) {
      best_lcm = lcm_v;
      best = v;
    }
  }

  cout << best << "\n";

  return 0;
}
