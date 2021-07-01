#ifndef __MYLIB__H__
#define __MYLIB__H__

namespace MyLib
{
    [[nodiscard]] int getAnswer() noexcept;
    [[nodiscard]] int echo(int val) noexcept;
} // namespace MyLib


#endif  //!__MYLIB__H__