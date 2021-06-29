cmake_minimum_required(VERSION 3.0)
project (MyLib)

add_library(mylib STATIC src/mylib.cpp)
target_include_directories(mylib PUBLIC include/)

add_executable(test test/main.cpp)
target_link_libraries(test PRIVATE mylib)
