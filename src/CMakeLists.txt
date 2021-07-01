cmake_minimum_required(VERSION 3.12)
project (
    mylib
    VERSION 0.4.0
    DESCRIPTION "An example project with CMake and conan"
    LANGUAGES CXX
)

add_library(mylib STATIC mylib.cpp)
target_compile_features(mylib PUBLIC cxx_std_17)
target_include_directories(mylib PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>)
