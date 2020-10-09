#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <string>
#include <cmath>
#include <limits>

using std::vector;
using std::string;
using std::pair;
using std::min;

struct Point {
  int x, y;
};

bool compareX (Point a, Point b) {
  return a.x < b.x;
}

bool compareY (Point a, Point b) {
  return a.y < b.y;
}

double dist (Point a, Point b) {
  return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}

double bruteForce(vector<Point> P, int low, int high) {  
  double min = std::numeric_limits<double>::max();  
  for (int i = low; i < high; ++i)  
    for (int j = i+1; j < high; ++j)  
      if (dist(P[i], P[j]) < min)  
        min = dist(P[i], P[j]);  
  return min;  
}

double stripClosest(vector<Point> strip, double d) {  
  double min = d;
  int size = strip.size();
    
  sort(strip.begin(), strip.end(), compareY);  
  
  // Pick all points one by one and try the next points till the difference  
  // between y coordinates is smaller than d.  
  // This is a proven fact that this loop runs at most 6 times  
  for (int i = 0; i < size; ++i)  
    for (int j = i+1; j < size && (strip[j].y - strip[i].y) < min; ++j)  
      if (dist(strip[i],strip[j]) < min)  
        min = dist(strip[i], strip[j]);  
  
  return min;  
}

double closestUtil(vector<Point> P, int low, int high)  
{  
  // If there are 2 or 3 points, then use brute force  
  if (high - low <= 3)  
    return bruteForce(P, low, high);  
  
  // Find the middle point  
  int mid = (low + high) / 2;  
  Point midPoint = P[mid];  
  
  // Consider the vertical line passing  
  // through the middle point calculate  
  // the smallest distance dl on left  
  // of middle point and dr on right side  
  double dl = closestUtil(P, low, mid);  
  double dr = closestUtil(P, mid, high);  
  
  // Find the smaller of two distances  
  double d = min(dl, dr);  
  
  // Build an array strip[] that contains  
  // points close (closer than d)  
  // to the line passing through the middle point  
  vector<Point> strip; 
  for (int i = low; i < high; i++)  
    if (abs(P[i].x - midPoint.x) < d)  
      strip.push_back(P[i]);  

  // Find the closest points in strip.  
  // Return the minimum of d and closest  
  // distance is strip[]  
  return min(d, stripClosest(strip, d));  
} 

double minimal_distance(vector<int> x, vector<int> y) {
  //write your code here
  vector<Point> P(x.size());
  for(int i = 0; i < x.size(); i++)
    P[i].x = x[i], P[i].y = y[i];
  sort(P.begin(), P.end(), compareX);
  return closestUtil(P, 0, P.size());
}

int main() {
  size_t n;
  std::cin >> n;
  vector<int> x(n);
  vector<int> y(n);
  for (size_t i = 0; i < n; i++) {
    std::cin >> x[i] >> y[i];
  }
  std::cout << std::fixed;
  std::cout << std::setprecision(9) << minimal_distance(x, y) << "\n";
}
