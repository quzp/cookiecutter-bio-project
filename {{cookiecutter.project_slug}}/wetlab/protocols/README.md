# protocols/

标准操作流程（SOP）。一个方法一个 `.md` 文件，文件名用小写下划线，例如：

```
organoid_differentiation.md
lentivirus_packaging.md
rna_extraction_trizol.md
10x_library_prep.md
```

约定：

- 每个协议文件顶部写版本号与修订日期，修订时在文件末尾的"修订记录"追加一行，
  不要删除旧内容——已经按旧版本做过的实验需要能追溯。
- 试剂写明厂家与货号，设备写明型号，这些是方法学部分要用的。
- 实验记录里引用协议时写明版本，例如 `protocol: organoid_differentiation.md v1.2`。

新建协议时复制 `TEMPLATE_protocol.md`。
