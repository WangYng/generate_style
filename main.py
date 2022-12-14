# 生成文本样式
import os.path
import re

from env import generate_file_dir, text_style_file, text_color_arr, text_font_arr, text_weight_arr, box_decoration_file, \
    box_decoration_color_arr, box_decoration_border_radius_arr

text_style_template = \
    '''\
// This file is automatically generated. DO NOT EDIT, all your changes would be lost.

import 'package:flutter/material.dart';

class %s {
%s\
}

extension TextStyleHelper on TextStyle{
  TextStyle withOpacity(double opacity) {
    return copyWith(color: color.withOpacity(opacity));
  }
} 
'''

text_style_template_1 = \
    '''\
  static final color%s_font%s = TextStyle(color: Color(0xFF%s), fontSize: %s);
'''

text_style_template_2 = \
    '''\
  static final color%s_font%s_weight%s = TextStyle(color: Color(0xFF%s), fontSize: %s, fontWeight: FontWeight.w%s);
'''


box_decoration_template = \
    '''\
// This file is automatically generated. DO NOT EDIT, all your changes would be lost.

import 'package:flutter/material.dart';

class %s {
%s\
}

extension BoxDecorationHelper on BoxDecoration {
  BoxDecoration withBoxShadow({color: const Color.fromRGBO(0, 0, 0, 0.1), blurRadius: 6, offset: const Offset(0, 0)}) {
    return copyWith(boxShadow: [BoxShadow(color: color, blurRadius: blurRadius, offset: offset)]);
  }
}
'''

box_decoration_template_1 = \
    '''\
  static final color%s_borderRadius%s = BoxDecoration(color: Color(0xFF%s), borderRadius: BorderRadius.circular(%s));
'''


# 下划线转驼峰
def text_to_hump(text):
    arr = re.split('[-_ ]', text)
    res = ''
    j = 0
    for i in arr:
        if j == 0:
            res = i[0].upper() + i[1:]
        else:
            res = res + i[0].upper() + i[1:]
        j += 1
    return res


def generate_text_style():
    file_path = os.path.join(generate_file_dir, text_style_file)
    if not os.path.exists(generate_file_dir):
        os.mkdir(generate_file_dir)
    with open(file_path, 'wb') as file:
        # 类名
        class_name = text_to_hump(os.path.basename(file_path).split(".")[0])

        # 内容
        content_arr = []

        # 样式一
        for color in text_color_arr:
            for font in text_font_arr:
                content_arr.append(text_style_template_1 % (color, font, color, font))

        # 样式二
        for text_weight in text_weight_arr:
            for color in text_color_arr:
                for font in text_font_arr:
                    content_arr.append(text_style_template_2 % (color, font, text_weight, color, font, text_weight))

        file.write((text_style_template % (class_name, "\n".join(content_arr))).encode(encoding='utf-8'))
        print("生成文本样式完成")


def generate_box_decoration():
    file_path = os.path.join(generate_file_dir, box_decoration_file)
    if not os.path.exists(generate_file_dir):
        os.mkdir(generate_file_dir)
    with open(file_path, 'wb') as file:
        # 类名
        class_name = text_to_hump(os.path.basename(file_path).split(".")[0])

        # 内容
        content_arr = []

        # 样式一
        for color in box_decoration_color_arr:
            for radius in box_decoration_border_radius_arr:
                content_arr.append(box_decoration_template_1 % (color, radius, color, radius))

        file.write((box_decoration_template % (class_name, "\n".join(content_arr))).encode(encoding='utf-8'))
        print("生成盒子样式完成")


if __name__ == '__main__':
    generate_text_style()
    generate_box_decoration()
