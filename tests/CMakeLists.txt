cmake_minimum_required(VERSION 3.1)
project(mylibTest CXX)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake OPTIONAL)

enable_testing()
find_package(CppUTest MODULE REQUIRED)
if(NOT TARGET mylib)
    find_package(mylib CONFIG REQUIRED)
endif()

add_executable(unit_test_lib main.cpp)
target_link_libraries(unit_test_lib 
    PRIVATE 
        Ruvi-D::mylib 
        CppUTest::CppUTest
        CppUTest::CppUTestExt
)

add_test(NAME mylib.unit_tests COMMAND unit_test_lib)
