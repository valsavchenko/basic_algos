#include <gtest/gtest.h>

#include "Counter.h"

using namespace counter;

TEST(Sample, Case1)
{
    const auto count = count_unique_modulo_values({-11, -7, -5, -1, 0, 1, 3});
    EXPECT_EQ(6, count);
}

TEST(Sample, Case2)
{
    const auto count = count_unique_modulo_values({-11, 11});
    EXPECT_EQ(1, count);
}

TEST(Sample, Case3)
{
    const auto count = count_unique_modulo_values({-11, -7, 11, 11});
    EXPECT_EQ(2, count);
}
