#include "Counter.h"

#include <cassert>
#include <algorithm>

namespace counter
{

Count count_unique_absolute_values(const NonDecreasingIntegers& values) noexcept
{
    // Take advantage of the fact that the input is totally ordered:
    // First of, adjacent equivalent elements at an end are simply equal
    // Secondly, equivalent head and tail elements sum up to zero
    assert(std::is_sorted(values.cbegin(), values.cend()));

    Count equivalent{ 0 };
    // For-loop to reduce the scope of variables, which point to the current head and tail
    for (Integer h{ 0 }, t{ static_cast<Integer>(values.size()) - 1 };
         h < t;
         /**/)
    {
        if (values[h] == values[h + 1])
        { // Count an equivalent pair at the head
            ++equivalent;
            ++h;
            continue;
        }

        if (values[t - 1] == values[t])
        { // Count an equivalent pair at the tail
            ++equivalent;
            --t;
            continue;
        }

        const Integer sum{ values[h] + values[t] };
        if (0 == sum)
        { // Count an equivalent pair at the ends
            ++equivalent;
            ++h;
            --t;
        }
        else if (sum < 0)
        { // Skip a unique element at the head
            ++h;
        }
        else // 0 < sum
        { // Skip a unique element at the tail
            --t;
        }
    }

    // Count uniques by excluding total number of duplicate pairs
    const Count count{ static_cast<Count>(values.size()) - equivalent };
    return count;
}

}
