## Linux build
```
conan install .. --profile ../profiles/linux_gcc_10_release
mkdir build && cd build
conan install ..
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . -- -j
```

## Beaglebone Black build
```
sudo apt install gcc-arm-linux-gnueabihf  g++-arm-linux-gnueabihf crossbuild-essential-armhf
conan install .. --profile ../profiles/bb_armhf_release --build=cpputest
cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++ -DCMAKE_C_COMPILER=arm-linux-gnueabihf-gcc
cmake --build . -- -j
```
