cmake_minimum_required(VERSION 3.12)
project(OutOfSourcePackageTest CXX)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)
find_package(mylib REQUIRED)

add_executable(testapp main.cpp)
target_link_libraries(testapp PRIVATE mylib::mylib) #Note namespace appears to be broken with conan package
