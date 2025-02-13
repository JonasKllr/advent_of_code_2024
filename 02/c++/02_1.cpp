#include "csv_helpers.hpp"

bool is_increasing(const int &first_element, const int &secont_element);
bool is_decreasing(const int &first_element, const int &secont_element);
bool max_three_apart(const int &first_element, const int &secont_element);

std::tuple<std::vector<bool>, std::vector<bool>> find_safe_levels(const std::vector<int> &data)
{
    std::vector<bool> increasing_tracker(data.size() - 1, false);
    std::vector<bool> decreasing_tracker(data.size() - 1, false);

    for (int i = 0; i < data.size() - 1; i++)
    {
        if (is_increasing(data[i], data[i + 1]) and max_three_apart(data[i], data[i + 1]))
        {
            increasing_tracker[i] = true;
        }
        if (is_decreasing(data[i], data[i + 1]) and max_three_apart(data[i], data[i + 1]))
        {
            decreasing_tracker[i] = true;
        }
    }
    return std::make_tuple(increasing_tracker, decreasing_tracker);
}

bool is_increasing(const int &first_element, const int &secont_element)
{
    return (secont_element - first_element) > 0;
}

bool is_decreasing(const int &first_element, const int &secont_element)
{
    return (secont_element - first_element) < 0;
}

bool max_three_apart(const int &first_element, const int &secont_element)
{
    return (abs(secont_element - first_element) <= 3);
}

bool all_levels_are_safe(const std::vector<bool>& data)
{
    return (std::all_of(data.begin(), data.end(), [](bool v) { return v; }));
}

void pop_element_from_vector(std::vector<int> &vector, const int &element_position)
{
    vector.erase(vector.begin() + element_position);
}

bool false_in_adjacent_elements(const std::vector<bool> &tracker)
{
    bool in_adjacent_elements = false;
    for (int i = 0; i < tracker.size() - 1; i++)
    {
        if (tracker[i] == false and tracker[i + 1] == false)
        {
            in_adjacent_elements = true;
        }
    }
    return in_adjacent_elements;
}

int find_id_of_false_in_adjacent_elements(const std::vector<bool> &tracker)
{
    int id_of_false_in_adjacent_elements = 0;
    for (int i = 0; i < tracker.size() - 1; i++)
    {
        if (tracker[i] == false and tracker[i + 1] == false)
        {
            id_of_false_in_adjacent_elements = i;
        }
    }
    return id_of_false_in_adjacent_elements;
}

int main()
{
    std::string path = "/home/jonas/coding_practice/advent_of_code/02/advent_of_code-02.csv";
    std::vector<std::vector<int>> data = read_csv(path);

    int safe_counter = 0;
    for (int i = 0; i < data.size(); i++)
    {
        std::vector<bool> increasing_tracker{}, decreasing_tracker{};
        std::tie(increasing_tracker, decreasing_tracker) = find_safe_levels(data[i]);

        if (all_levels_are_safe(increasing_tracker) or all_levels_are_safe(decreasing_tracker))
        {
            safe_counter++;
        }
        else
        {
            // ### second part ###
            for (int j = 0; j < data[i].size(); j++)
            {
                std::vector<int> temp_row = data[i];
                pop_element_from_vector(temp_row, j);

                std::vector<bool> increasing_tracker_damped{}, decreasing_tracker_damped{};
                std::tie(increasing_tracker_damped, decreasing_tracker_damped) = find_safe_levels(temp_row);

                if (all_levels_are_safe(increasing_tracker_damped) or all_levels_are_safe(decreasing_tracker_damped))
                {
                    safe_counter++;
                    break;
                }
            }
        }
    }
    std::cout << safe_counter << "\n";
}
