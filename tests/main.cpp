#include "mylib/mylib.hpp"
#include "CppUTest/TestHarness.h"
#include "CppUTest/CommandLineTestRunner.h"

TEST_GROUP(myLibTest){};

TEST(myLibTest, testTheAnswer)
{
    CHECK_EQUAL(42,MyLib::getAnswer());
}

TEST(myLibTest, testEcho)
{
    CHECK_EQUAL(42,MyLib::echo(42));
}

int main(int ac, char** av)
{
    return RUN_ALL_TESTS(ac, av);
}
