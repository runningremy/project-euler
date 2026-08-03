#include <iostream>

int main() {
	int i = 1;
	int j = 0;
	while (i < 1000) {
		if (i % 3 == 0 || i % 5 == 0) {
			j = j + i;
			i++;
		} else {
			i++;
		}
	}
	std::cout << j << std::endl;
	//std::cout << "Hello, World!" << std::endl;
	return 0;
}
