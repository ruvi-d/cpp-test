set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR ARM)

# Clang target triple
SET(TARGET armv7hf-linux-gnueabihf)

# specify the cross compiler
SET(CMAKE_C_COMPILER_TARGET ${TARGET})
SET(CMAKE_C_COMPILER clang-11)
SET(CMAKE_CXX_COMPILER_TARGET ${TARGET})
SET(CMAKE_CXX_COMPILER clang++-11)
SET(CMAKE_ASM_COMPILER_TARGET ${TARGET})
SET(CMAKE_ASM_COMPILER clang-11)

set(CMAKE_SYSROOT "/home/ruvinda/x-tools/arm-cortex_a8-linux-gnueabihf/arm-cortex_a8-linux-gnueabihf/sysroot")
SET(ARCH_FLAGS "-target armv7hf-linux-gnueabihf -mcpu=cortex-a8 -mfpu=neon -mfloat-abi=hard -fuse-ld=lld-11")
SET(CMAKE_C_FLAGS ${ARCH_FLAGS})
SET(CMAKE_CXX_FLAGS ${ARCH_FLAGS})

# C++ linking is broken
