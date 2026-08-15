#include <stdio.h>
#include <unistd.h>
#include <string.h>

void rev(char* revBinary) 
{
	int l = 0;
	int r = strlen(revBinary) - 1;
	char t;

	while (l < r) {
		t = revBinary[l];
		revBinary[l] = revBinary[r];
		revBinary[r] = t;

		l++;
		r++;
	}
}

int main()
{
	float number = 53.14159;
	float numerator;
	float quotient = 1;
	int integer, sign;
	char revBinary[50] = "";
	char binary;
	
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
			strcat(revBinary, "1");
		} else {
			strcat(revBinary, "0");
		}
		numerator = (int) quotient;
	}
	
	//printf("%s\n", revBinary);

	rev(revBinary);

	printf("%s", revBinary);
	return 0;
	//printf("The number we are working with is %.5f.\n", number);
	//printf("The sign is equal to %d.\n", sign);
	//printf("The integer part of %.5f is %d.\n", number, integer);
}
