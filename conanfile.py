from conans import ConanFile, CMake

class RegexConan(ConanFile):
    name = "mylib"
    version = "0.2.0"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake_find_package", "cmake_paths"
        
    def requirements(self):
        self.requires("cpputest/4.0")

    def export_sources(self):
        self.copy("src/*")                 # -> copies all .cpp files from working dir to a "source" dir
        self.copy("tests/*")
        self.copy("app/*")
        self.copy("include/*")
        self.copy("CMakeLists.txt")

    def build(self):
        cmake = CMake(self)                # CMake helper auto-formats CLI arguments for CMake
        cmake.configure()                  # cmake -DCMAKE_TOOLCHAIN_FILE=conantoolchain.cmake
        cmake.build()                      # cmake --build .  

    def package(self):
        self.copy("*.hpp", dst="include", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["mylib"]
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libsdirs = ["lib"]
