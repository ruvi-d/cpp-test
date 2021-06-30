cmake_minimum_required(VERSION 3.11...3.20)
project (
    MyLib
    VERSION 0.1
    DESCRIPTION "An example project with CMake"
    LANGUAGES CXX
)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

set(CMAKE_CXX_STANDARD 17 CACHE STRING "The C++ standard to use")
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

enable_testing()

add_subdirectory(src)

add_subdirectory(tests)
