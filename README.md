## Linux build
### To build conan package
```
conan create . demo/demo -pr profiles/linux_gcc_10_release
```
### To build with cmake
```
mkdir build && cd build
conan install .. -pr ../profiles/linux_gcc_10_release
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . -- -j
ctest
```
### To build out of source test app
```
cd app && mkdir build
conan install . -pr ../profiles/linux_gcc_10_release --install-folder build
cmake . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build/ -- -j
```
### Regular development on src/
```
mkdir build && cd build
conan install .. -pro ../profiles/linux_gcc_10_release
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
# conan install .. -pr ../profiles/bb_armhf_release --build=cpputest
conan install .. -pr ../profiles/bb_armhf_release
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++ -DCMAKE_C_COMPILER=arm-linux-gnueabihf-gcc
cmake --build . -- -j
```
### To build out of source test app
```
cd app && mkdir build-bb
conan install . -pr ../profiles/bb_armhf_release --install-folder build-bb
cmake . -B build-bb/ -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++
cmake --build build-bb/ -- -j
```

#### Misc conan commands
```
# Search
conan search mylib/0.3.0@ -r ruvi-remote
conan search mylib/0.3.0@ -r ruvi-remote  --table=conan_matrix.html

# Installing dependancies
conan install glog/0.4.0@ -g markdown
conan install . -pr arm --install-folder build-bb 
conan install . --install-folder build -b missing (build from source if prebuilts are missing)

# Install and build (based on conanfile build)
conan install . -pr profiles/bb_armhf_release --install-folder build-bb 
conan build . --install-folder build-bb 

# Override profile
conan install .. -pr arm --install-folder build-bb -s build_type=Debug

# Run in-source package development
conan source . --source-folder=tmp/source
conan install . --install-folder=temp/build [-pr]
conan build . --source-folder=tmp/source --build-folder=tmp/build  
## can do smaller build steps too --config, --build, --install 
conan package . --source-folder=tmp/source --build-folder=tmp/build --package-folder=tmp/package
conan export-pkg . user/testing --package-folder=tmp/package
conan test test_package mylib/0.3.0@ruvi/demo 

# Upload
conan remote add ruvi-remote https://ruvi.jfrog.io/artifactory/api/conan/ruvi-conan
conan user -p #### -r ruvi-remote ruvinda.dhambarage@nagarro.com
conan upload mylib/0.2.0@ruvi/* -r ruvi-remote --all

## -e to override environment variable, -o to override options
```
