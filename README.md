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

## Beaglebone Black build
### Prerequisites 
```
sudo apt install gcc-arm-linux-gnueabihf  g++-arm-linux-gnueabihf crossbuild-essential-armhf
```
### Cross build
Test execution should be disabled for this profile
```
conan install .. --profile ../profiles/bb_armhf_release --build=cpputest
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++ -DCMAKE_C_COMPILER=arm-linux-gnueabihf-gcc
cmake --build . -- -j
```
