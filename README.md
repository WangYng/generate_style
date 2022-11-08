# generate_style
生成Flutter项目模板样式代码

## 最终生成的代码
```dart
class MyTextStyle {
  static final color333333_font10 = TextStyle(color: Color(0xFF333333), fontSize: 10);

  static final color333333_font11 = TextStyle(color: Color(0xFF333333), fontSize: 11);

  static final color333333_font12 = TextStyle(color: Color(0xFF333333), fontSize: 12);
  
  // ....
}


class MyBoxDecoration {
  static final colorFFFFFF_borderRadius3 = BoxDecoration(color: Color(0xFFFFFFFF), borderRadius: BorderRadius.circular(3));

  static final colorFFFFFF_borderRadius4 = BoxDecoration(color: Color(0xFFFFFFFF), borderRadius: BorderRadius.circular(4));

  static final colorFFFFFF_borderRadius5 = BoxDecoration(color: Color(0xFFFFFFFF), borderRadius: BorderRadius.circular(7));
  
  // ...
}
```

## 用法
1. 在项目根目录生成 env.py
```python

# 生成的样式文件存放路径
generate_file_dir = 'xxx/generated/'

# 生成的文本样式
text_style_file = "my_text_style.dart"
text_color_arr = [
    "333333",
]
text_font_arr = [
    "10",
    "11",
    "12"
]
text_weight_arr = [
    "500"
]

# 生成盒子样式
box_decoration_file = "my_box_decoration.dart"
box_decoration_color_arr = [
    "FFFFFF"
]
box_decoration_border_radius_arr = [
    "3",
    "4",
    "5"
]
```

2. 运行main.py
