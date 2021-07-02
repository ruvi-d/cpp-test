from conans import ConanFile, CMake, tools

class MyLibConan(ConanFile):
    name = "mylib"
    description = "An example project with CMake and conan"
    license = "https://github.com/ruvi-d/cpp-test/blob/main/LICENSE"
    url = "https://github.com/ruvi-d/cpp-test"
    exports = ["LICENSE"]
    version = "0.5.0"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake_find_package", "cmake_paths"
        
    def build_requirements(self):
        if not tools.cross_building(self):
            self.build_requires("cpputest/4.0")

    def export_sources(self):
        self.copy("src/*")                 # -> copies all .cpp files from working dir to a "source" dir
        self.copy("tests/*")
        self.copy("profiles/*")
        self.copy("CMakeLists.txt")

    def build(self):
        cmake = CMake(self)                # CMake helper auto-formats CLI arguments for CMake
        cmake.configure()                  # cmake -DCMAKE_TOOLCHAIN_FILE=conantoolchain.cmake
        cmake.build()                      # cmake --build .  
        if not tools.cross_building(self):
            cmake.test()

    def package(self):
        self.copy("*.hpp", dst="include", src="src/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["mylib"]
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libsdirs = ["lib"]
