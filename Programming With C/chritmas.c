struct point {int x, y;};
struct line {point p1, p2;};
int main() {
	line L1 = {{3, 5},{21, 33}};
	point P = {0, 12}, Q = {60, 50};
	line L2 = {P, L1.p2};
}