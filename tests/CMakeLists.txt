find_package(CppUTest REQUIRED)

add_executable(testlib main.cpp)
target_link_libraries(testlib 
                PRIVATE 
                    mylib 
                    CppUTest::CppUTest CppUTest::CppUTestExt
)

add_test(NAME mylibtests COMMAND testlib)
