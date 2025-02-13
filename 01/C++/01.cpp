#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include "csv_helpers.hpp"

void sort_list(std::vector<int> &list)
{
    std::sort(list.begin(), list.end());
}

std::vector<int> subtract_element_wise(const std::vector<int> &left_list, const std::vector<int> &right_list)
{
    std::vector<int> differences(left_list.size());
    std::transform(left_list.begin(), left_list.end(), right_list.begin(), differences.begin(), std::minus<int>());
    return differences;
}

int calculate_total_distance(const std::vector<int> &differences)
{
    int result = 0;
    for (int i = 0; i < differences.size(); i++)
    {
        result += std::abs(differences[i]);
    }
    return result;
}

int main()
{
    std::string path = "/home/jonas/coding_practice/advent_of_code/01/advent_of_code.csv";
    std::vector<std::vector<int>> data = read_csv(path);

    std::vector<int> left_list{}, right_list{};
    std::tie(left_list, right_list) = extract_lists(data);

    sort_list(left_list);
    sort_list(right_list);

    std::vector<int> differences = subtract_element_wise(left_list, right_list);

    int result = calculate_total_distance(differences);
    std::cout << result << "\n";
}