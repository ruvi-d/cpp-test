## Build conan package
### Native GCC-10 build
```console
$ conan create . user/test -pr conan-profiles/x86_64_gcc_10 -b missing
```
### Native clang-11 build
```console
$ conan create . user/test -pr conan-profiles/x86_64_clang_11 -b missing
```
### arm-linux-gnueabihf build
```console
$ conan create . user/test -pr conan-profiles/arm_gcc_gnueabihf -b missing
```
### arm-cortex_a8-linux-gnueabihf build
```console
$ conan create . user/test -pr conan-profiles/arm_gcc_cortex_a8 -b missing
```

## Build out-of-source test app
Assuming that mylib has been uploaded to local cache or remote
### Native GCC-10 build
```console
$ cd app && mkdir build
$ conan install . -pr ../conan-profiles/x86_64_gcc_10 -if build
$ cmake . -B build -DCMAKE_BUILD_TYPE=Release
$ cmake --build build/
```
### Native clang-11 build
```console
$ cd app && mkdir build-llvm
$ conan install . -pr ../conan-profiles/x86_64_clang_11 -if build-llvm
$ cmake -B build-llvm -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=../cmake/clang-11_x86_64.cmake .
$ cmake --build build-llvm/
```
### arm-linux-gnueabihf build
```console
$ cd app && mkdir build-arm
$ conan install . -pr ../conan-profiles/arm_gcc_gnueabihf -if build-arm
$ cmake -B build-arm -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=../cmake/gcc_arm-linux-gnueabihf_toolchain.cmake .
$ cmake --build build-arm/
```
### arm-cortex_a8-linux-gnueabihf build
```console
$ cd app && mkdir build-a8
$ conan install . -pr ../conan-profiles/arm_gcc_cortex_a8 -if build-a8
$ cmake -B build-a8 -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=../cmake/gcc_arm-cortex_a8-linux-gnueabihf_toolchain.cmake .
$ cmake --build build-a8/
```


## Misc Conan commands
```console
# Search
$ conan search mylib/0.3.0@ -r ruvi-remote
$ conan search mylib/0.3.0@ -r ruvi-remote  --table=conan_matrix.html

# Installing dependancies
$ conan install glog/0.4.0@ -g markdown
$ conan install . -pr arm -if build-arm 
$ conan install . -if build -b missing

# Install and build (based on conanfile build)
$ conan install . -pr arm -if build-arm 
$ conan build . -if build-arm 

# Override profile
$ conan install .. -pr arm -if build-bb -s build_type=Debug

# Run in-source package development
$ conan source . -sf tmp/src
$ conan install . -if temp/build [-pr]
$ conan build . -sf tmp/src -bf tmp/build  
## can do smaller build steps too --config, --build, --test, --install 
$ conan package . -sf tmp/src -bf tmp/build -pf tmp/package
$ conan export-pkg . user/test -pf tmp/package
$ conan test test_package mylib/0.3.0@user/test 

# Upload to remote repo
$ conan remote add ruvi-remote https://ruvi.jfrog.io/artifactory/api/conan/ruvi-conan
$ conan user -p #### -r ruvi-remote ruvinda.dhambarage@nagarro.com
$ conan upload mylib/0.2.0@ruvi/* -r ruvi-remote --all

## Set/Override configs
### -e to override environment variable
### -o to override package options
### -s to override package settings
```
