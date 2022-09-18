# Google Python 开源代码风格指南


- [Google Python 开源代码风格指南](#google-python-开源代码风格指南)
  - [语言规范](#语言规范)
    - [pylint](#pylint)
    - [Import](#import)
    - [包](#包)

## 语言规范

### pylint

pylint是一个在Python源代码中查找bug的工具，可以捕获容易忽视的错误, 例如输入错误, 使用未赋值的变量等。

### Import

仅对包和模块使用导入,而不单独导入函数或者类。`typing`模块例外。

1. 使用 import x 来导入包和模块.
2. 使用 from x import y , 其中x是包前缀, y是不带前缀的模块名.
3. 使用 from x import y as z, 如果两个要导入的模块都叫做y或者y太长了.
4. 仅当缩写 z 是通用缩写时才可使用 import y as z.(比如 np 代表 numpy.)

例如, 模块 `sound.effects.echo` 可以用如下方式导入:

```python
from sound.effects import echo
echo.EchoFilter(input, output, delay=0.7, atten=4)
```

### 包

使用模块的全路径名来导入每个模块。

所有的新代码都应该用完整包名来导入每个模块.

应该像下面这样导入:

yes:

``` python
# 在代码中引用完整名称 absl.flags (详细情况).
import absl.flags
from doctor.who import jodie

FLAGS = absl.flags.FLAGS
# 在代码中仅引用模块名 flags (常见情况).
from absl import flags
from doctor.who import jodie

FLAGS = flags.FLAGS
```

No: (假设当前文件和 jodie.py 都在目录 doctor/who/ 下)
```python
# 没能清晰指示出作者想要导入的模块和最终被导入的模块.
# 实际导入的模块将取决于 sys.path.
import jodie
```

不应假定主入口脚本所在的目录就在 sys.path 中，虽然这种情况是存在的。当主入口脚本所在目录不在 sys.path 中时，代码将假设 import jodie 是导入的一个第三方库或者是一个名为 jodie 的顶层包，而不是本地的 jodie.py