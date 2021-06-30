cmake_minimum_required(VERSION 3.11...3.20)
project(OutOFSourcePackageTest CXX)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)
find_package(mylib REQUIRED)

add_executable(testapp main.cpp)
target_link_libraries(testapp PRIVATE mylib::mylib)
