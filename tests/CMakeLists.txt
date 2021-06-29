find_package(GTest REQUIRED)
add_executable(testlib main.cpp)
target_link_libraries(testlib PRIVATE mylib GTest::GTest GTest::Main)
gtest_discover_tests(testlib)
