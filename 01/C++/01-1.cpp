#include "csv_helpers.hpp"

int main()
{
    std::string path = "/home/jonas/coding_practice/advent_of_code/01/advent_of_code.csv";
    std::vector<std::vector<int>> data = read_csv(path);

    std::vector<int> left_list{}, right_list{};
    std::tie(left_list, right_list) = extract_lists(data);

    int sum = 0;
    for (int i = 0; i < left_list.size(); i++)
    {
        int value = left_list[i];
        int value_counter = 0;
        for (int j = 0; j < left_list.size(); j++)
        {
            if (right_list[j] == value)
            {
                value_counter++;
            }
        }
        sum += value * value_counter;
    }
    std::cout << sum << "\n";
}