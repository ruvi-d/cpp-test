cmake_minimum_required(VERSION 3.12)
project (
    mylib
    VERSION 0.5.2
    DESCRIPTION "An example project with CMake and conan"
    LANGUAGES CXX
    )

include(${CMAKE_BINARY_DIR}/conan_paths.cmake OPTIONAL)

add_library(mylib STATIC mylib.cpp)
target_compile_features(mylib PUBLIC cxx_std_17)
target_include_directories(mylib PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
    )

add_library(Ruvi-D::mylib ALIAS mylib)

install(TARGETS mylib 
        EXPORT mylibTargets
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib
        RUNTIME DESTINATION bin
        )

include(CMakePackageConfigHelpers)
write_basic_package_version_file(
    mylibConfigVersion.cmake
    VERSION ${PACKAGE_VERSION}
    COMPATIBILITY AnyNewerVersion
    )

install(EXPORT mylibTargets
        DESTINATION lib/cmake/mylib
        FILE mylibTarget.cmake
        NAMESPACE Ruvi-D::
        )

install(DIRECTORY include/mylib
        DESTINATION include
        )

configure_file(mylibConfig.cmake.in mylibConfig.cmake @ONLY)

install(FILES "${CMAKE_CURRENT_BINARY_DIR}/mylibConfig.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/mylibConfigVersion.cmake"
        DESTINATION lib/cmake/MyLib
        )
