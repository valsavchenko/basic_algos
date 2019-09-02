#ifndef COUNTER_H
#define COUNTER_H

#include <vector>

namespace counter
{

using Count = unsigned long long;
using Integer = long long;
using NonDecreasingIntegers = std::vector<Integer>;

Count count_unique_absolute_values(const NonDecreasingIntegers& values) noexcept;

}

#endif // COUNTER_H
