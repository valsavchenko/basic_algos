#include "Counter.h"

#include <algorithm>
#include <iterator>
#include <string>
#include <iostream>

using namespace counter;

int main(int argc, const char** argv)
{
    NonDecreasingIntegers values{};
    values.reserve(argc - 1);

    try
    {
        std::transform(argv + 1, argv + argc, std::back_inserter<NonDecreasingIntegers>(values),
            [](const char* arg)
            {
                return std::stol(arg);
            });
    }
    catch (const std::exception& e)
    {
        std::cout << "The elements are not integers!\n";
        return 1;
    }

    if (!std::is_sorted(values.cbegin(), values.cend()))
    {
        std::cout << "The elements are not ordered!\n";
        return 2;
    }

    const auto count = count_unique_absolute_values(values);
    std::cout << "Number of unique elements is " << count << "\n";
    return 0;
}
