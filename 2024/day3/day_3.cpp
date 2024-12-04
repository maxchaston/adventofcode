#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cctype>
#include <cmath>

enum oper { doop, dont, mul, nothing };

typedef struct match {
	oper type;
	int num1; // for mul, undefined for other operators
	int num2;
} match;

// return format is num found and number of characters matched (0 if no match)
// feels more sane than log10 on the result, extra handling needed for 0
std::pair<int, int> check_nums(std::string str) {
	int num = 0;
	bool match = false;
	int i;
	for (i=0; i<3 && std::isdigit(str[i]); i++) {
		match = true;
		num = num*10;
		num += str[i]-'0';
	}
	if (!match) 
		return {-1, 0};
	return {num, i+1};
}

match check_match(std::string str) {
	if (str.substr(0, sizeof("do()")-1) == "do()") {
		return {doop, 0, 0};
	}
	if (str.substr(0, sizeof("don't()")-1) == "don't()") {
		return {dont, 0, 0};
	}
	if (str.substr(0, sizeof("mul(")-1) == "mul(") {
		int num1 = 0;
		int num2 = 0;
		// followed by 1-3 nums, a comma, then 1-3 nums, then a closing bracket
		std::string numstr;

		// first nums
		numstr = str.substr(sizeof("mul(")-1);
		std::pair numcheck_result = check_nums(numstr);
		if (numcheck_result.second == 0) // no match found
			return {nothing, 0, 0};
		num1 = numcheck_result.first;

		// comma
		numstr = numstr.substr(numcheck_result.second-1);
		if (numstr[0] != ',')
			return {nothing, 0, 0};

		// last nums
		numstr = numstr.substr(1);
		numcheck_result = check_nums(numstr);
		if (numcheck_result.second == 0) // no match found
			return {nothing, 0, 0};
		num2 = numcheck_result.first;

		// closing bracket
		numstr = numstr.substr(numcheck_result.second-1);
		if (numstr[0] != ')')
			return {nothing, 0, 0};
		return {mul, num1, num2};
		
	}
	return {nothing, 0, 0};
}

std::string read_file() {
	std::ifstream file ("bigboy.txt", std::ios::in);
	std::stringstream buf;
	buf << file.rdbuf();
	file.close();
	return buf.str();
}

int main() {
	int count=0;
	std::string s = read_file();

	// Part 1
	for (int i=0; i<s.length(); i++)
	{
		match curr_match = check_match(s.substr(i));
		if (curr_match.type == mul) {
			count+=curr_match.num1*curr_match.num2;
		}
	}
	std::cout << count << std::endl;

	// Part 2
	bool enabled = true;
	count = 0;
	for (int i=0; i<s.length(); i++)
	{
		match curr_match = check_match(s.substr(i));
		if (curr_match.type == doop)
			enabled = true;
		if (curr_match.type == dont)
			enabled = false;
		if (curr_match.type == mul && enabled) {
			count+=curr_match.num1*curr_match.num2;
		}
	}
	std::cout << count << std::endl;
	return 0;
}

/**
General C++ solution, not massively fast.
Seems like substrings are not particularly performant.
I think going iterative until it stops working is the way to go.
**/
