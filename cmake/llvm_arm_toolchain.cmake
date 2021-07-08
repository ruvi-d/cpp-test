set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR ARM)

# Clang target triple
SET(TARGET arm-linux-gnueabihf)

# specify the cross compiler
SET(CMAKE_C_COMPILER_TARGET ${TARGET})
SET(CMAKE_C_COMPILER clang-11)
SET(CMAKE_CXX_COMPILER_TARGET ${TARGET})
SET(CMAKE_CXX_COMPILER clang++-11)
SET(CMAKE_ASM_COMPILER_TARGET ${TARGET})
SET(CMAKE_ASM_COMPILER clang-11)

#set(CMAKE_SYSROOT "/home/ruvinda/x-tools/arm-cortex_a8-linux-gnueabihf/arm-cortex_a8-linux-gnueabihf/sysroot")
set(CMAKE_SYSROOT /)
SET(ARCH_FLAGS "-target arm-linux-gnueabihf")
SET(CMAKE_C_FLAGS ${ARCH_FLAGS})
SET(CMAKE_CXX_FLAGS ${ARCH_FLAGS})

# C++ linking is broken
