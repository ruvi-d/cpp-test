cmake_minimum_required(VERSION 3.12)
project (
    mylib
    VERSION 0.4.0
    DESCRIPTION "An example project with CMake and conan"
    LANGUAGES CXX
)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake OPTIONAL)

add_library(mylib STATIC mylib.cpp)
target_compile_features(mylib PUBLIC cxx_std_17)
target_include_directories(mylib PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>)

add_library(Ruvi-D::mylib ALIAS mylib)

install(TARGETS mylib EXPORT mylibTargets
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib
        RUNTIME DESTINATION bin
        INCLUDES DESTINATION include)

install(EXPORT mylibTargets
        DESTINATION lib/cmake/mylib
        FILE mylibTargets.cmake
        NAMESPACE Ruvi-D::)

install(DIRECTORY include/mylib
        DESTINATION include)
