#include <mylib/mylib.hpp>
#include <gtest/gtest.h>

TEST(myLibTest, testTheAnswer)
{
    ASSERT_EQ(MyLib::getAnswer(), 42);
}
