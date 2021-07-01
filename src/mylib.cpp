#include "mylib/mylib.hpp"

namespace MyLib
{
   [[nodiscard]] int getAnswer() noexcept{
      return 42;
   }
   
   [[nodiscard]] int echo(int val) noexcept{
      return val;
   }
} // namespace MyLib
