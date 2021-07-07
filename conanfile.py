from conans import ConanFile, CMake, tools

class MyLibConan(ConanFile):
    name = "mylib"
    version = "0.5.3"
    description = "An example project with CMake and conan"
    license = "https://github.com/ruvi-d/cpp-test/blob/main/LICENSE"
    url = "https://github.com/ruvi-d/cpp-test"
    exports = ["LICENSE"]
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake_find_package", "cmake_paths", "cmake"
        
    def build_requirements(self):
        self.build_requires("cpputest/4.0")

    def _configure_cmake(self):
        cmake = CMake(self)                 # CMake helper auto-formats CLI arguments for CMake
        #cmake.definitions["SOME_DEFINITION"] = "VALUE"
        cmake.configure()                   # cmake -DCMAKE_TOOLCHAIN_FILE=conantoolchain.cmake
        return cmake

    def export_sources(self):
        self.copy("src/*")                 # -> copies all .cpp files from working dir to a "source" dir
        self.copy("tests/*")
        self.copy("profiles/*")
        self.copy("CMakeLists.txt")

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()                      # cmake --build .  
        if not tools.cross_building(self):
            cmake.test()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["mylib"]
