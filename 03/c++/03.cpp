#include <string>
#include <iostream>
#include <regex>
#include <algorithm>
#include <fstream>

std::string read_in_text(const std::string &path)
{
    std::ifstream stream{path};
    std::string temp_data{};
    std::string data{};

    while (std::getline(stream, temp_data))
    {
        data.append(temp_data);
    }
    stream.close();
    return data;
}

void remove_chars_from_string(std::string &str, std::string charsToRemove)
{
    for (unsigned int i = 0; i < charsToRemove.size(); ++i)
    {
        str.erase(remove(str.begin(), str.end(), charsToRemove[i]), str.end());
    }
}

int main()
{
    std::string input_data = read_in_text("/home/jonas/coding_practice/advent_of_code/03/input.txt");
    std::regex substring("mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don't\\(\\)");
    std::smatch match;

    int result{0};
    bool do_multiplication = true;

    while (std::regex_search(input_data, match, substring))
    {
        std::string extracted_string = match.str(0);
        remove_chars_from_string(extracted_string, "mul()");
        input_data = match.suffix().str();

        if (extracted_string == "do")
        {
            do_multiplication = true;
        }
        else if (extracted_string == "don't")
        {
            do_multiplication = false;
        }

        if ((do_multiplication == true) and (extracted_string.find(",") != -1))
        {
            int position_of_comma = extracted_string.find(",");
            std::string left_number_string = extracted_string.substr(0, position_of_comma);
            std::string right_number_string = extracted_string.substr(position_of_comma + 1);

            int left_number_int = std::stoi(left_number_string);
            int right_number_int = std::stoi(right_number_string);

            result += left_number_int * right_number_int;
        }
    }
    std::cout << result << "\n";
}