# 待完成
1. ~~将keyboard_movement修改为事件触发, KEYDOWN和KEYUP之间的间隔就是长按的事件~~(暂时不用)
2. 先完成creep的移动功能, 实现碰撞效果(要和多个小兵碰撞并且和英雄碰撞)
3. 搞明白groups类的功能, 再搞明白super().__init__()的功能
    并且改掉main.py30行不太正确的creep生成方法

#  笔记
显示1个像素对应实际3个像素: 英雄是96个像素显示32*32的图像

# 程序构思
creep_group.sprites 好像是一个方法, 搞明白这个究竟返回什么
Groups.sprites() 有括号才是返回的方法
