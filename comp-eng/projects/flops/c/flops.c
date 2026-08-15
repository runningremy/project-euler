#include <stdio.h>
#include <unistd.h>
#include <string.h>

void rev(char* intBinary)
{
	char t[100];
	int len = strlen(intBinary);
	int i = 0;

	while (len > 0)
		t[i++] = intBinary[len-- - 1];
	t[i] = '\0';

	strcpy(intBinary, t);

}
int big(float number)
{
	float numerator;
	float quotient = 1;
	int integer, sign;
	char intBinary[100];
	
	if (number < 0)
	{
		sign = 1;
	} else {
		sign = 0;
	}

	integer = number;

	numerator = integer;
	
	while (numerator > 0) {
		quotient = numerator / 2;
		if (quotient > (int) quotient)
		{
			strcat(intBinary, "1");
		} else {
			strcat(intBinary, "0");
		}
		numerator = (int) quotient;
	}
	
	rev(intBinary);
	printf("%s\n", intBinary);
	return 0;
}

int main()
{
	int counter = 0;
	int test = 1;
	while (counter < 1000000) {
		big(test);
		counter++;
		test++;
		sleep(1);
	}
	return 0;
}
