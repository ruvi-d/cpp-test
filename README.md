## Native GCC10 build
### To build conan package
```
conan create . user/test -pr profiles/linux_gcc_10_release
```
### To build with CMake
```
mkdir build
conan install . -pr profiles/linux_gcc_10_release -if build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . -- -j
ctest
```
### To build out of source test app
```
cd app && mkdir build
conan install . -pr ../profiles/linux_gcc_10_release -if build
cmake . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build/ -- -j
```


## AM335X cross compiling build
### Prerequisites: toolchain
```
sudo apt install gcc-arm-linux-gnueabihf  g++-arm-linux-gnueabihf crossbuild-essential-armhf
```
### To build conan package
```
conan create . user/test -pr profiles/bb_armhf_release
```
### To build with CMake
```
mkdir build-arm
conan install . -pr profiles/bb_armhf_release -b missing -if build-arm
cmake . -B build-arm/ -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++ -DCMAKE_C_COMPILER=arm-linux-gnueabihf-gcc
cmake --build build-arm/ -- -j
```
### To build out of source test app
```
cd app && mkdir build-arm
conan install . -pr ../profiles/bb_armhf_release -if build-arm
cmake . -B build-arm/ -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++
cmake --build build-arm/ -- -j
```

## Misc Conan commands
```
# Search
conan search mylib/0.3.0@ -r ruvi-remote
conan search mylib/0.3.0@ -r ruvi-remote  --table=conan_matrix.html

# Installing dependancies
conan install glog/0.4.0@ -g markdown
conan install . -pr arm --install-folder build-arm 
conan install . --install-folder build -b missing

# Install and build (based on conanfile build)
conan install . -pr profiles/bb_armhf_release -if build-arm 
conan build . -if build-arm 

# Override profile
conan install .. -pr arm --install-folder build-bb -s build_type=Debug

# Run in-source package development
conan source . -sf tmp/src
conan install . -if temp/build [-pr]
conan build . -sf tmp/src -bf tmp/build  
## can do smaller build steps too --config, --build, --test, --install 
conan package . -sf tmp/src -bf tmp/build -pf tmp/package
conan export-pkg . user/test -pf tmp/package
conan test test_package mylib/0.3.0@user/test 

# Upload to remote repo
conan remote add ruvi-remote https://ruvi.jfrog.io/artifactory/api/conan/ruvi-conan
conan user -p #### -r ruvi-remote ruvinda.dhambarage@nagarro.com
conan upload mylib/0.2.0@ruvi/* -r ruvi-remote --all

## Set/Override configs
### -e to override environment variable
### -o to override package options
### -s to override package settings
```
