#include <stdio.h>

void main(void)
{
	int i, j;
	i = 1;
	j = 0;
	while (i < 1000) {
		if (i % 3 == 0 || i % 5 == 0) {
			j = j + i;
			i++;
		} else {
			i++;
		}
	}
	printf("%d\n", j);
}
