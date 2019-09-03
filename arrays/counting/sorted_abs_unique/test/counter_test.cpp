#include <gtest/gtest.h>

#include "Counter.h"

#include <limits>

using namespace counter;

TEST(Sample, Case1)
{
    const auto count = count_unique_absolute_values({ -11, -7, -5, -1, 0, 1, 3 });
    EXPECT_EQ(6, count);
}

TEST(Sample, Case2)
{
    const auto count = count_unique_absolute_values({ -11, 11 });
    EXPECT_EQ(1, count);
}

TEST(Sample, Case3)
{
    const auto count = count_unique_absolute_values({ -11, -7, 11, 11 });
    EXPECT_EQ(2, count);
}

TEST(Tiny, Empty)
{
    const auto count = count_unique_absolute_values({});
    EXPECT_EQ(0, count);
}

TEST(Tiny, LonePositive)
{
    const auto count = count_unique_absolute_values({ 1 });
    EXPECT_EQ(1, count);
}

TEST(Tiny, LoneZero)
{
    const auto count = count_unique_absolute_values({ 0 });
    EXPECT_EQ(1, count);
}

TEST(Tiny, LoneNegative)
{
    const auto count = count_unique_absolute_values({ -1 });
    EXPECT_EQ(1, count);
}

TEST(Homogeneous, UniquePositives)
{
    const NonDecreasingIntegers values{ 0, 8, 13, 62, 7292 };
    const auto count = count_unique_absolute_values(values);
    EXPECT_EQ(values.size(), count);
}

TEST(Homogeneous, DuplicatesAtHeadPositives)
{
    const auto count = count_unique_absolute_values({0, 0, 0, 1, 2, 3, 4});
    EXPECT_EQ(5, count);
}

TEST(Homogeneous, DuplicatesInMiddlePositives)
{
    const auto count = count_unique_absolute_values({0, 1, 2, 2, 2, 2, 2, 3, 4, 5});
    EXPECT_EQ(6, count);
}

TEST(Homogeneous, DuplicatesAtTailPositives)
{
    const auto count = count_unique_absolute_values({0, 1, 2, 3, 3});
    EXPECT_EQ(4, count);
}

TEST(Homogeneous, TotallyDuplicatePositives)
{
    const auto count = count_unique_absolute_values({ 77, 77, 77, 77, 77, 77 });
    EXPECT_EQ(1, count);
}

TEST(Homogeneous, HugePositives)
{
    const Integer huge{ std::numeric_limits<Integer>::max() };
    const auto count = count_unique_absolute_values({ huge - 7, huge - 5, huge - 3, huge - 2, huge - 1 });
    EXPECT_EQ(5, count);
}

TEST(Homogeneous, UniqueNegatives)
{
    const NonDecreasingIntegers values{ -62, -13, -8 };
    const auto count = count_unique_absolute_values(values);
    EXPECT_EQ(values.size(), count);
}

TEST(Homogeneous, DuplicatesAtHeadNegatives)
{
    const auto count = count_unique_absolute_values({ -72, -72, -72, -55, -44, -4, -1 });
    EXPECT_EQ(5, count);
}

TEST(Homogeneous, DuplicatesInMiddleNegatives)
{
    const auto count = count_unique_absolute_values({ -7, -6, -5, -5, -5, -4, -3, -1 });
    EXPECT_EQ(6, count);
}

TEST(Homogeneous, DuplicatesAtTailNegatives)
{
    const auto count = count_unique_absolute_values({ -11, -7, -5, -2, -2, -2, -2 });
    EXPECT_EQ(4, count);
}

TEST(Homogeneous, TotallyDuplicateNegatives)
{
    const auto count = count_unique_absolute_values({ -13, -13 });
    EXPECT_EQ(1, count);
}

TEST(Homogeneous, HugeNegatives)
{
    const Integer huge{ std::numeric_limits<Integer>::min() };
    const auto count = count_unique_absolute_values({ huge + 1, huge + 2, huge + 3, huge + 5, huge + 7, huge + 11 });
    EXPECT_EQ(6, count);
}

TEST(Assorted, DuplicateHalves)
{
    const auto count = count_unique_absolute_values({-10, -10, -10, 0, 0, 0, 0});
    EXPECT_EQ(2, count);
}

TEST(Assorted, MirroredIdenticalHalves)
{
    const auto count = count_unique_absolute_values({ -7, -7, -7, -7, 7, 7 });
    EXPECT_EQ(1, count);
}

TEST(Assorted, MirroredDuplicateHalves)
{
    const auto count = count_unique_absolute_values({-3, -3, -3, -2, -2, -1, 1, 1, 1, 2, 2, 3});
    EXPECT_EQ(3, count);
}
