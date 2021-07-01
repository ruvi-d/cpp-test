cmake_minimum_required(VERSION 3.12)
project(mylib)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

set(CMAKE_CXX_STANDARD 17 CACHE STRING "The C++ standard to use")
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_subdirectory(src)

enable_testing()
add_subdirectory(tests)
