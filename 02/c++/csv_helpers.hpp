#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>

std::vector<std::vector<std::string>> remove_trailing_character(std::vector<std::vector<std::string>> &data);
std::vector<std::vector<int>> convert_data_to_int(std::vector<std::vector<std::string>> &data_string);
std::vector<std::vector<std::string>> remove_empty_characters(std::vector<std::vector<std::string>> &data);
std::vector<std::vector<std::string>> remove_character_from_number(std::vector<std::vector<std::string>> &data);

std::vector<std::vector<int>> read_csv(const std::string file_name)
{
    std::vector<std::vector<std::string>> csv_data{};
    std::ifstream file_stream(file_name);
    std::string line{};

    while (std::getline(file_stream, line))
    {
        std::stringstream ss(line);
        std::vector<std::string> row{};
        std::string value{};

        while (std::getline(ss, value, ','))
        {
            row.push_back(value);
        }
        csv_data.push_back(row);
    }
    file_stream.close();
    csv_data = remove_trailing_character(csv_data);
    csv_data = remove_character_from_number(csv_data);
    csv_data = remove_empty_characters(csv_data);
    return convert_data_to_int(csv_data);
}

std::vector<std::vector<std::string>> remove_trailing_character(std::vector<std::vector<std::string>> &data)
{
    for (int i = 0; i < data.size(); i++)
    {
        std::vector<std::string> temp_row = data[i];
        for (int j = 0; j < data[i].size(); j++)
        {
            if (temp_row[j] == "\r")
            {
                temp_row.erase(temp_row.begin() + j);
            }
        }
        data[i] = temp_row;
    }
    return data;
}

std::vector<std::vector<std::string>> remove_character_from_number(std::vector<std::vector<std::string>> &data)
{
    std::string character_to_remove = "\r";
    for (int i = 0; i < data.size(); i++)
    {
        std::vector<std::string> temp_row = data[i];
        for (int j = 0; j < data[i].size(); j++)
        {
            if (temp_row[j].find(character_to_remove) != std::string::npos)
            {
                temp_row[j] = temp_row[j].substr(0, temp_row[j].size() - character_to_remove.size());
            }
        }
        data[i] = temp_row;
    }
    return data;
}

std::vector<std::vector<std::string>> remove_empty_characters(std::vector<std::vector<std::string>> &data)
{
    for (int i = 0; i < data.size(); i++)
    {
        std::vector<std::string> temp_row = data[i];
        for (int j = 0; j < data[i].size(); j++)
        {
            if (temp_row[j].empty())
            {
                temp_row.erase(temp_row.begin() + j, temp_row.begin() + (temp_row.size()));
                break;
            }
        }
        data[i] = temp_row;
    }
    return data;
}

std::vector<std::vector<int>> convert_data_to_int(std::vector<std::vector<std::string>> &data_string)
{
    std::vector<std::vector<int>> data_int{};
    for (int i = 0; i < data_string.size(); i++)
    {
        std::vector<int> row(data_string[i].size());
        for (int j = 0; j < data_string[i].size(); j++)
        {
            row[j] = std::stoi(data_string[i][j]);
        }
        data_int.push_back(row);
    }
    return data_int;
}

std::tuple<std::vector<int>, std::vector<int>> extract_lists(const std::vector<std::vector<int>> &combined_lists)
{
    std::vector<int> left_list{}, right_list;
    for (int i = 0; i < combined_lists.size(); i++)
    {
        left_list.push_back(combined_lists[i][0]);
        right_list.push_back(combined_lists[i][1]);
    }
    return std::make_tuple(left_list, right_list);
}