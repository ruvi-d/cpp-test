## Linux build
### To build conan package
```
conan create . demo/demo --profile profiles/linux_gcc_10_release
```
### To build with cmake
```
mkdir build && cd build
conan install .. --profile ../profiles/linux_gcc_10_release
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . -- -j
ctest
```
### To build with conan
```
conan install . -pr profiles/linux_gcc_10_release --install-folder build
conan build . --build-folder build
```
### To build out of source test app
```
cd app && mkdir build && cd build
conan install .. --profile ../../profiles/linux_gcc_10_release
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . -- -j
```
### Regular development on src/
```
mkdir build && cd build
conan install .. --profile ../profiles/linux_gcc_10_release
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . -- -j
```

## Beaglebone Black build
### Prerequisites (crosscompiler toolchain)
```
sudo apt install gcc-arm-linux-gnueabihf  g++-arm-linux-gnueabihf crossbuild-essential-armhf
```
### To build conan package
```
conan create . demo/demo --profile profiles/bb_armhf_release
```
### Cross build
Test execution should be disabled for this profile
```
# First time build run with --build=cpputest
# conan install .. --profile ../profiles/bb_armhf_release --build=cpputest
conan install .. --profile ../profiles/bb_armhf_release
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++ -DCMAKE_C_COMPILER=arm-linux-gnueabihf-gcc
cmake --build . -- -j
```
### To build out of source test app
```
cd app && mkdir build && cd build
conan install .. --profile ../../../profiles/bb_armhf_release
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++
cmake --build . -- -j
```
