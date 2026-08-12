//here is a project that takes an integer input and returns the binary value

#include <stdio.h>
#include <math.h>


double baseTwo(double argument)
{
	double base2_log = log2(argument);
	double log_floor = floor(base2_log);
	//double difference = base2_log - log_floor;
	
	return base2_log;
}


int main()
{
	double base2_log = baseTwo(7.0);
	printf("%lf\n", base2_log);

	return 0;
}
