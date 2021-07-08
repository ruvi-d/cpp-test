SET(target armv7hf-linux-gnueabihf)
SET(CMAKE_C_COMPILER clang-11)
SET(CMAKE_C_COMPILER_TARGET ${target})
SET(CMAKE_CXX_COMPILER clang++-11)
SET(CMAKE_CXX_COMPILER_TARGET ${target})

SET(ARCH_FLAGS "-mcpu=cortex-a8 -mfpu=neon -mfloat-abi=hard -static -fuse-ld=lld-11")
set(CMAKE_C_FLAGS_INIT ${ARCH_FLAGS})
set(CMAKE_CXX_FLAGS_INIT ${ARCH_FLAGS})
